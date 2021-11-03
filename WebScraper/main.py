import requests
from Scoring.score import score
from Data.sources import read_file
from bs4 import BeautifulSoup

urls = read_file('urls.txt')
keywords = read_file('keywords.txt')


def scrape(source_url):
    response = requests.get(source_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find_all(['p', 'h1', 'h2', 'h3'])
    return content


scraped = scrape(urls[0])
article_score = score(scraped, keywords)
print(article_score)
