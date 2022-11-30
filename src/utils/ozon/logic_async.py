from models.reply_models import Review, Product
from utils.other_utils import parse_cookies, generate_headers
import aiohttp
import asyncio
import random
import json
from dispatcher import bot


async def pagination(startup_data, user_id: str,pagination_last_timestamp = 0, pagination_last_uuid = None):
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
            #logging.warning(f'Что-то пошло не так - {response.status}')
            await bot.send_message(user_id, f'WARNING - Что-то пошло не так - {response.status}')
            return None


async def get_new_reviews(startup_data, user_id: str):
    review_list = []
    pagination_last_timestamp = 0
    pagination_last_uuid = None
    flag = True
    while flag:
        try:
            reviews, pagination_last_timestamp, pagination_last_uuid = await pagination(startup_data, user_id, pagination_last_timestamp, pagination_last_uuid)
            review_list.extend(reviews)
            if pagination_last_uuid == None:
                flag = False
        except:
            break
    if len(review_list) > 0:
        await bot.send_message(f'INFO - Новых отзывов: {len(review_list)} шт.')
        #logging.info(f'Новых отзывов: {len(review_list)} шт.')
        return review_list
    else:
        await bot.send_message(f'INFO - Новых отзывов нет.')
        #logging.info(f'Новых отзывов нет.')
        return None


async def get_all_reviews(startup_data, user_id: str):
    url = 'https://seller.ozon.ru/api/v3/review/list'
    payload = json.dumps({
        "filter": {
            "interaction_status": [
                "ALL"
            ]
        },
        "sort": {
            "sort_by": "PUBLISHED_AT",
            "sort_direction": "DESC"
        },
        "company_id": startup_data['company_id'],
        "company_type": "seller",
        "with_counters": True,
        "pagination_last_timestamp": 0,
        "pagination_last_uuid": None
    })
    async with aiohttp.ClientSession() as session:
        response = await session.post(url=url, headers=startup_data['headers'], data=payload)
        if response.status == 200:
            json_raw = await response.json()
            reviews = json_raw['result']
            try:
                count_reviews = json_raw['counters']['PROCESSED']
                #logging.info(f'Всего отзывов: {count_reviews} шт.')
                await bot.send_message(f'INFO - Всего отзывов: {count_reviews} шт.')
                return reviews
            except:
                #logging.info('Отзывов нет.')
                await bot.send_message('INFO - Отзывов нет.')
                pass
        else:
            #logging.warning(f'Что-то пошло не так - {response.status}')
            await bot.send_message(f'WARNING - Что-то пошло не так - {response.status}')
            return None


async def parse_reviews(reviews):
    reviews_list = []
    if reviews:
        for review_item in reviews:
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


async def reply_to_review(review, company_id, headers):
    if review.rating >= 4:
        url = 'https://seller.ozon.ru/api/review/comment/create'
        payload = json.dumps({
            "company_id": company_id,
            "company_type": "seller",
            "parent_comment_id": 0,
            "review_uuid": review.uuid,
            "text": await review.generate_reply()
        })

        async with aiohttp.ClientSession() as session:
            await asyncio.sleep(random.randint(4, 7))
            response = await session.post(url=url, headers=headers, data=payload)
            if response.status == 200:
                #logging.info(f'Отвечено на отзыв: {review.title}')
                return True
            else:
                #logging.warning(f'Что-то пошло не так. Проблема с ответом на отзыв: {review.title}')
                return False
    else:
        return False


async def gather_data(reviews, startup_data, company_id):
    if reviews:
        for idx, review in enumerate(reviews):
            if await reply_to_review(review, company_id=startup_data['company_id'], headers=startup_data['headers']):
                #logging.info(f'Отвечено на {idx+1}/{len(reviews)}')
                pass
            else:
                continue
    #logging.info(f'Процесс ответа на отзывы закончен.')


async def generate_startup_data(company_id: str):
    group_value, access_token, refresh_token, user_id, cf_bm = await parse_cookies('ozon/db/cookies.json')
    headers = await generate_headers(company_id, group_value, access_token, refresh_token, user_id, cf_bm)
    data = {
        'company_id': company_id,
        'headers': headers
    }
    return data


async def get_new_reviews_bot(user_id: str):
    startup_data = await generate_startup_data()
    reviews_raw = await get_new_reviews(startup_data)
    reviews_list = await parse_reviews(reviews_raw)
    await gather_data(reviews_list, startup_data)


async def get_all_reviews_bot():
    startup_data = await generate_startup_data()
    reviews_raw = await get_all_reviews(startup_data)
    reviews_list = await parse_reviews(reviews_raw)
