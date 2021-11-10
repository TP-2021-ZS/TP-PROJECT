import requests
from bs4 import BeautifulSoup


class WebScrubber:
    def __init__(self):
        pass

    def get_web_page_soup(self, url):
        page = str(BeautifulSoup(requests.get(url).content, features='lxml'))
        return BeautifulSoup(page, 'lxml')

    def get_string_by_tags(self, soup, tags):
        return self.__soup_to_string_by_tags(soup, tags)

    def __get_string_by_tag_name(self, soup, tag_name: str) -> str:
        tags = soup.find_all(tag_name)
        stripped_tags = ''

        for tag in tags:
            for descendant in tag.descendants:
                stripped_tags += str(descendant.string)
                stripped_tags += ' '

        return stripped_tags

    def __soup_to_string_by_tags(self, soup, tags: list):
        string_builder = ''

        for tag in tags:
            string_builder += self.__get_string_by_tag_name(soup, tag)

        return self.__sanitize_string(string_builder)

    def __sanitize_string(self, string: str) -> str:
        return string.lower().replace(', ', ' ').replace(' , ', ' ').replace(' . ', ' ')


#Example usage
'''
c = WebScrubber()

s = c.get_web_page_soup("https://akcie.sk/tesla-predbehla-facebook-a-prekonala-trhovu-hodnotu-1-biliona/")
tags = ['p','h1','h2','h3']

nadpisy = c.get_string_by_tags(s, ['h1', 'h2', 'h3'])
texty = c.get_string_by_tags(s, ['p'])

print(nadpisy)
print(texty)
'''