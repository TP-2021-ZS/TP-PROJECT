import requests
import csv
import re
from Scoring.score import score
from bs4 import BeautifulSoup

url = "https://akcie.sk/tesla-predbehla-facebook-a-prekonala-trhovu-hodnotu-1-biliona/"


def scrape(source_url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find_all(['p', 'h1', 'h2', 'h3'])
    return content


scraped = scrape(url)


def write_to_csv(list_input):
    # The scraped info will be written to a CSV here.
    try:
        with open("dataSet.csv", "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen)
            csv_writer.writerow(list_input)
    except:
        return False


article_score = score(scraped)
print(article_score)
