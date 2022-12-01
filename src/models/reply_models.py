from random import choice
from utils.other_utils import read_json

class Product():
    def __init__(self, title, url, offer_id):
        self.title = title
        self.url = url
        self.offer_id = offer_id


class Review(Product):
    def __init__(self, id, sku, text, published_at, rating, interaction_status, author_name, uuid, product: Product):
        super().__init__(product.title, product.url, product.offer_id)
        self.id = id
        self.sku = sku
        self.text = text
        self.published_at = published_at
        self.rating = rating
        self.interaction_status= interaction_status
        self.author_name = author_name
        self.uuid = uuid

    async def generate_reply(self, user_positive: str, goodslist: str):
        response_list = await read_json(goodslist)
        goods_list = await read_json(user_positive)
        recommendation_code = None

        for i in goods_list:
            ms_code: str = i['code_ms']
            modification_code = ms_code.split('/')[0]
            if modification_code == self.offer_id:
                recommendation_code = i['recommendation']
                break

        if not recommendation_code:
            recommendation_code = '246088986, 459113390, 245959082'

        greetings_list = choice(response_list['greetings'])
        thanks_list = choice(response_list['thanks'])
        main_text_list = choice(response_list['main_text'])
        recommendation_list = choice(response_list['recommendation'])
        instruction_list = choice(response_list['instruction'])
        wish_list = choice(response_list['goodbye'])

        phrase = f'{greetings_list} {thanks_list} {self.title} {main_text_list} {recommendation_list} {recommendation_code}. {instruction_list} {wish_list}'
        return phrase