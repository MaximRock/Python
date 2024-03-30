import requests
from models import *
import csv


class ParseWb:
    def __init__(self):
        self.page: int = 1
        self.query: str = 'видеокарта для пк'
        self.sort: str = 'priceup'

    @property
    def headers(self):
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'https://www.wildberries.ru',
            'Referer': 'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort=pricedown&search=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D0%B0+%D0%B4%D0%BB%D1%8F+%D0%BF%D0%BA',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.766 (beta) Yowser/2.5 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'x-queryid': 'qid39947372171092157720240321104634',
        }
        return headers

    def params(self):
        params = {
            'appType': '1',
            'curr': 'rub',
            'dest': '-1257786',
            'page': self.page,
            'query': self.query,
            'resultset': 'catalog',
            'sort': self.sort,
            'spp': '30',
            'suppressSpellcheck': 'false',
        }
        return params

    def url(self):
        url = requests.get('https://search.wb.ru/exactmatch/ru/common/v5/search',
                           headers=self.headers,
                           params=self.params())
        return url

    @staticmethod
    def __create_csv():
        with open('wd-data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'Название', 'бренд', 'цена', 'рейтинг'])

    @staticmethod
    def __save_csv(items: Items):
        with open('wd-data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            for product in items.products:
                writer.writerow([
                    product.id,
                    product.name,
                    product.brand,
                    product.sizes[0].price.product,
                    product.reviewRating
                ])

    def parse(self):
        self.page = 1
        self.__create_csv()
        while True:
            if not self.url().json().get('params'):
                self.page += 1
                # print(Items.parse_obj(self.url().json()['data']))
                items_info = Items.parse_obj(self.url().json()['data'])
                self.__save_csv(items_info)
            else:
                break


if __name__ == "__main__":
    ParseWb().parse()

# 'page': '100',
# priceup
