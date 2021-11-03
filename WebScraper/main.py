import requests
from Scoring.score import score
from Data.sources import read_url_file
from bs4 import BeautifulSoup

urls = read_url_file('urls.txt')


def scrape(source_url):
    response = requests.get(source_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find_all(['p', 'h1', 'h2', 'h3'])
    return content


scraped = scrape(urls[0])
article_score = score(scraped)
print(article_score)
