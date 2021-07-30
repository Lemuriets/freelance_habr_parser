import asyncio

import asyncio

import requests
from bs4 import BeautifulSoup

from req import get_response


class Pagination:
    def __init__(self, url: str) -> None:
        self.url = url
        self.pagination_pages = []
        self.mainloop = asyncio.get_event_loop()

        self._start_mainloop()

    def _get_page_count(self, url: str) -> int:
        html_data = get_response(url).text

        soup = BeautifulSoup(html_data, 'html.parser')
        pagination_div = soup.find_all('div', class_='pagination')

        if not pagination_div:
            return 0

        pagination_text = BeautifulSoup(pagination_div[0].text, 'html.parser')

        links = pagination_text.text.split(' ')

        for i in links:
            if i.isdigit():
                max_pag_number = int(i)

        return max_pag_number

    async def _get_list_futures(self, url: str, page_count: int) -> None:
        return [self.mainloop.run_in_executor(None, get_response, f'{url}?page={i}') for i in range(1, page_count)]

    async def _get_responses(self, page_count: int):
        for page in await self._get_list_futures(self.url, page_count):
            asyncio.ensure_future(page)
            self.pagination_pages.append(await page)
        return self.pagination_pages

    def _start_mainloop(self) -> None:
        try:
            self.mainloop.run_until_complete(self._get_responses(self._get_page_count(self.url)))
        except KeyboardInterrupt:
            self.mainloop.close()


a = Pagination('https://freelance.habr.com/tasks?')
print(a.pagination_pages)