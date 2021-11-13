import requests
from bs4 import BeautifulSoup


def scrape(source_url, tags):
    response = requests.get(source_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find_all(tags)
    return content


def tags_to_string(text):
    strippedTags = ''
    for tag in text:
        for descen in tag.descendants:
            strippedTags += str(descen.string).strip()
            strippedTags += ' '
    return strippedTags
