import asyncio

import requests
from bs4 import BeautifulSoup

from lib.validate_url import Validation


class Parser:
    def __init__(self, url: str) -> None:
        self.url = url

    def _main(self) -> None:
        Validation(self.url)


# price - {div, class = task__price-icon}, {span, class = negotiated_price}
# order - {div, class = content-list content-list_tasks}, {li, class = content-list__item}
# task_title - {div, class = task__title}, {a}