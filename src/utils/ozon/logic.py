import http.client, random
from models.reply_models import Review, Product
from time import sleep
from utils.other_utils import generate_headers, parse_cookies
from core.config import settings
import json

async def get_reviews(company_id, group_value, access_token, refresh_token, user_id, cf_bm):
    conn = http.client.HTTPSConnection("seller.ozon.ru")
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
      "company_id": company_id,
      "company_type": "seller",
      "with_counters": True,
      "pagination_last_timestamp": 0,
      "pagination_last_uuid": None
    })
    headers = await generate_headers(company_id, group_value, access_token, refresh_token, user_id, cf_bm)
    conn.request("POST", "/api/v3/review/list", payload, headers)
    response = conn.getresponse()
    if response.getcode() == 200:
        data = response.read().decode('utf-8')
        json_raw = json.loads(data)
        reviews = json_raw['result']
        if reviews:
            not_viewed = json_raw['counters']['NOT_VIEWED']
            print(f'Новых отзывов: {not_viewed} шт.')
            return reviews
        else:
            print('Новых отзывов нет.')
    else:
        print(f'Что-то пошло не так - {response.getcode()}')
        return None


async def parse_reviews(reviews):
    reviews_list = []
    if reviews:
        for review_item in reviews:
            # logging.info(review_item)
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
            # logging.info(f'{review.generate_reply()}\n')


async def reply_to_reviews(reviews_array, company_id, group_value, access_token, refresh_token, user_id, cf_bm):
    conn = http.client.HTTPSConnection("seller.ozon.ru")

    if reviews_array:
        for idx, review in enumerate(reviews_array):
            if review.rating == 5 or review.rating == 4:
                payload = json.dumps({
                    "company_id": company_id,
                    "company_type": "seller",
                    "parent_comment_id": 0,
                    "review_uuid": review.uuid,
                    "text": await review.generate_reply()
                })
                headers = await generate_headers(company_id, group_value, access_token, refresh_token, user_id, cf_bm)
                conn.request("POST", "/api/review/comment/create", payload, headers)
                res = conn.getresponse()
                data = res.read().decode("utf-8")
                json_raw = json.loads(data)
                if json_raw['result'] == True:
                    sleep(random.randint(2,5))
                    print(f'Отвечено на {idx+1} из {len(reviews_array)} отзывов.')
                    continue
                else:
                    print(f'Не удалось ответить на отзыв: {res.read().decode("utf-8")}')


async def main_func():
    group_value, access_token, refresh_token, user_id, cf_bm = await parse_cookies('ozon/db/cookies.json')
    reviews_raw = await get_reviews(settings.TEST_COMPANY_ID, group_value, access_token, refresh_token, user_id, cf_bm)
    reviews_list = await parse_reviews(reviews_raw)
    await reply_to_reviews(reviews_list, settings.TEST_COMPANY_ID, group_value, access_token, refresh_token, user_id, cf_bm)


