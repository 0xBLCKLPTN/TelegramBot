from models.reply_models import Review, Product
from utils.other_utils import parse_cookies, generate_headers, find_cookies_file
from dispatcher import bot
from typing import Union
import aiohttp
import asyncio
import random
import json


class GetReviews:
    async def get_new_reviews_bot(self, user_id: str, company_id: str, cookies_filepath: str, list_of_products:str, recomend_file: str) -> None:
        '''
        Start function.

        Gets:
            - user_id: str for bot.send_message.
        '''
        startup_data = await self.generate_startup_data(user_id, company_id, cookies_filepath)
        reviews_raw = await self.get_new_reviews(user_id, startup_data)
        reviews_list = await self.parse_reviews(reviews_raw)
        await self.gather_data(reviews_list, startup_data, list_of_products, recomend_file)


    async def generate_startup_data(self, user_id: str, company_id: str, cookies_filepath: str) -> dict:
        '''
        Creating data with headers and company_id
        
        Gets:
            - user_id: str for bot.send_message.
            - company_id: str for headers generation
        
        Returns:
            - data: dict with headers and company_id

        '''
        
        group_value, access_token, refresh_token, user_id_b, cf_bm = await parse_cookies(cookies_filepath)
        headers = await generate_headers(company_id, group_value, access_token, refresh_token, user_id_b, cf_bm)
        
        data = {
            'company_id': company_id,
            'headers': headers
        }

        return data

    async def get_new_reviews(self, user_id, startup_data) -> Union[list, None]:
        review_list: list = []
        pagination_last_timestamp: int = 0
        pagination_last_uuid = None

        flag = True

        while flag:
            try:
                reviews, pagination_last_timestamp, pagination_last_uuid = await self.pagination(startup_data, user_id, pagination_last_timestamp, pagination_last_uuid)
                review_list.extend(reviews)
                if pagination_last_uuid == None:
                    flag = False
            except:
                pass
        if len(review_list) > 0:
            await bot.send_message(user_id, f'INFO - Новых отзывов: {len(review_list)} шт.')
            return review_list
        else:
            await bot.send_message(user_id, f'INFO - Новых отзывов нет.')
            return None


    async def gather_data(self, reviews_list, startup_data, list_of_products, rec_file) -> None:
        if reviews_list:
            for idx, review in enumerate(reviews_list):
                if await self.reply_to_review(review, list_of_products, rec_file, company_id=startup_data['company_id'], headers=startup_data['headers']):
                    print(f'Отвечено на {idx+1}/{len(reviews_list)}')
                else:
                    continue

    async def reply_to_review(self, review, list_of_products, rec_file, company_id, headers) -> bool:
        if review.rating >= 4:
            url = 'https://seller.ozon.ru/api/review/comment/create'
            payload = json.dumps({
                "company_id": company_id,
                "company_type": "seller",
                "parent_comment_id": 0,
                "review_uuid": review.uuid,
                "text": await review.generate_reply(list_of_products, rec_file)
            })

            async with aiohttp.ClientSession() as session:
                await asyncio.sleep(random.randint(4, 7))
                response = await session.post(url=url, headers=headers, data=payload)
                if response.status == 200:
                    print(f'Отвечено на отзыв: {review.title}')
                    return True
                else:
                    print(f'Что-то пошло не так. Проблема с ответом на отзыв: {review.title}')
                    return False
        return False


    async def parse_reviews(self, reviews_raw) -> Union[object, None]:
        reviews_list = []
        if reviews_raw:
            for review_item in reviews_raw:
                product = review_item['product']
                review = Review(review_item['id'],
                                review_item['sku'],
                                review_item['text'],
                                review_item['published_at'],
                                review_item['rating'],
                                review_item['interaction_status'],
                                review_item['author_name'],
                                review_item['uuid'],
                                Product(product['title'],
                                        product['url'],
                                        product['offer_id']
                                        )
                                )
                reviews_list.append(review)
            return reviews_list
        return None


    async def pagination(self, startup_data, user_id: str,
                         pagination_last_timestamp = 0,
                         pagination_last_uuid = None) -> Union[tuple, None]:

        url = 'https://seller.ozon.ru/api/v3/review/list'
        payload = json.dumps({
            "filter": {
                "interaction_status": [
                    "NOT_VIEWED"
                ]
            },
            "sort": {
                "sort_by": "PUBLISHED_AT",
                "sort_direction": "DESC"
            },
            "company_id": startup_data['company_id'],
            "company_type": "seller",
            "with_counters": True,
            "pagination_last_timestamp": pagination_last_timestamp,
            "pagination_last_uuid": pagination_last_uuid
        })

        async with aiohttp.ClientSession() as session:
            response = await session.post(url=url, headers=startup_data['headers'], data=payload)
            if response.status == 200:
                json_raw = await response.json()
                reviews = json_raw['result']
                pagination_last_timestamp = json_raw['pagination_last_timestamp']
                pagination_last_uuid = json_raw['pagination_last_uuid']

                return reviews, pagination_last_timestamp, pagination_last_uuid

            else:
                print(f'Что-то пошло не так - {response.status}')
                await bot.send_message(user_id, f'WARNING - Что-то пошло не так - {response.status}')
                return None
