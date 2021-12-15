#!/usr/bin/env python
#
# Generates the uBlock blacklist from urls.txt
#

from typing import List, AnyStr
from datetime import datetime


def main():
    urls = load_urls()
    generate_for_google(urls)
    generate_for_startpage(urls)


def header(name: str) -> List[AnyStr]:
    return [
        f'! Title: Search Blacklist - {name}',
        f'! Updated: {datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")}',
        '! Expires: 1 day (update frequency)',
        '! Homepage: https://github.com/tdbits/ublock-search-blacklist',
        '! License: https://github.com/tdbits/ublock-search-blacklist/blob/main/LICENSE'
    ]


def load_urls() -> List[AnyStr]:
    with open('urls.txt', 'r') as urls_file:
        urls = urls_file.readlines()

    return list(filter(lambda line: not line.startswith('#') and len(line) > 0, map(lambda line: line.strip(), urls)))


def generate_for_google(urls: List[AnyStr]) -> List[AnyStr]:
    blacklist = map(lambda url: f'google.*##.g:has(a[href*="{url}"])', urls)

    with open('google.txt', 'w') as blacklist_file:
        blacklist_file.write('\n'.join(header('Google')))
        blacklist_file.write('\n')
        blacklist_file.write('\n'.join(blacklist))


def generate_for_startpage(urls: List[AnyStr]) -> List[AnyStr]:
    blacklist = map(lambda url: f'startpage.*##.w-gl__result:has(a[href*="{url}"])', urls)

    with open('startpage.txt', 'w') as blacklist_file:
        blacklist_file.write('\n'.join(header('Startpage')))
        blacklist_file.write('\n')
        blacklist_file.write('\n'.join(blacklist))


if __name__ == '__main__':
    main()
