import requests
from Scoring.score import score
from Data.sources import read_file
from bs4 import BeautifulSoup
from googlesearch import search

TAGS = ['p', 'h1', 'h2', 'h3']
urls = read_file('urls.txt')
keywords = read_file('keywords.txt')


def scrape(source_url):
    response = requests.get(source_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find_all(TAGS)
    return content


def tags_to_string(tags):
    strippedTags = ''
    for tag in tags:
        for descen in tag.descendants:
            strippedTags += str(descen.string)
            strippedTags += ' '
    return strippedTags


scraped = scrape(urls[0])
text_content = tags_to_string(scraped)

#article_score = score(text_content, keywords)
#print(article_score)

query = 'intitle:"investíciu"'

for i in search(query, tld="sk", num=10, stop=10, pause=2):
    print(i)
