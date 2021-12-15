#!/usr/bin/env python
#
# Generates the uBlock blacklist from urls.txt
#

from typing import List, AnyStr


def main():
    urls = load_urls()
    generate_for_google(urls)
    generate_for_startpage(urls)


def load_urls() -> List[AnyStr]:
    with open('urls.txt', 'r') as urls_file:
        urls = urls_file.readlines()

    return list(filter(lambda line: not line.startswith('#') and len(line) > 0, map(lambda line: line.strip(), urls)))


def generate_for_google(urls: List[AnyStr]) -> List[AnyStr]:
    blacklist = map(lambda url: f'google.*##.g:has(a[href*="{url}"])', urls)

    with open('google.txt', 'w') as blacklist_file:
        blacklist_file.writelines('\n'.join(blacklist))


def generate_for_startpage(urls: List[AnyStr]) -> List[AnyStr]:
    blacklist = map(lambda url: f'startpage.*##.w-gl__result:has(a[href*="{url}"])', urls)

    with open('startpage.txt', 'w') as blacklist_file:
        blacklist_file.writelines('\n'.join(blacklist))


if __name__ == '__main__':
    main()
