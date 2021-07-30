from os import path

import requests

from gen_filename import gen_filename_by_url


def get_response(url: str, filter_url: str = None) -> requests.Response:
    if filter_url:
        url += f'?q={filter_url}'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    response = requests.get(url, headers=headers)

    return response
