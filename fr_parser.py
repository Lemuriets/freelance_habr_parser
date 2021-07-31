import asyncio
import datetime
import json

import requests
from bs4 import BeautifulSoup

from lib.validate_url import Validation
from lib.pagination import Pagination
from lib.json_worker import Json_worker


class Parser():
    def __init__(self, url: str, filter_url: str = '') -> None:
        self.url = url
        self.filter_url = filter_url
        self.ready_orders_dict = {}
        self.pag = Pagination(self.url, self.filter_url)

        super().__init__()

        self._main()

    def _main(self) -> None:
        Validation(self.url)
        self._parse()

    def _parse(self) -> None:
        counter = 0
        ready_dict = {}

        for resp in self.pag.pagination_pages:
            temp_parser = BeautifulSoup(resp.text, 'html.parser')
            orders = temp_parser.find_all('li', class_=['content-list__item', 'content-list__item content-list__item_marked'])

            for order in orders:
                task = order.findAll('a')[0].text
                price = order.findAll('span', class_=['count', 'negotiated_price'])[0].text
                date_published = order.findAll('span', class_='params__published-at icon_task_publish_at')[0].text
                order_responses = order.findAll('span', class_='params__responses icon_task_responses')[0].text if order.findAll('span', class_='params__responses icon_task_responses') else '0 откликов'
                technologies = list(map(lambda t: t.text, order.findAll('a', class_='tags__item_link')))

                counter += 1

                ready_order = {
                    'task': task,
                    'price': price,
                    'date_published': date_published,
                    'technologies': technologies,
                    'order_responses': order_responses
                }

                ready_dict[counter] = ready_order

        Json_worker(str(datetime.datetime.now())[:10:]).dump_dict(ready_dict)

    def start_parse(self) -> None:
        self._main()
