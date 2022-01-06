# This Python file uses the following encoding: utf-8
from Process.crawler import get_urls_known_source
from Process.crawler import get_urls_random_source
from Process.elastic import add_article
from Data.data_processor import write_array_to_file
from Data.data_processor import read_file
from Process.parser import scrape
from Process.parser import tags_to_string
from Process.score import score
from settings import settings
import pandas as pd


""" INIT - read settings """
keywords_scoring = read_file(settings.keywords_scoring)
keywords_search = read_file(settings.keywords_search)
known_urls = read_file(settings.known_urls)
blacklist_urls = read_file(settings.blacklist_urls)

""" GET ARTICLES URLS """
#articles_known = get_urls_known_source(settings.get_urls_known, known_urls, keywords_search, settings.date_after)
#articles_random = get_urls_random_source(settings.get_urls_random, keywords_search, blacklist_urls)

""" SAVE URLS TO FILE [Temporary] """
#write_array_to_file(articles_known, "known.txt")
#write_array_to_file(articles_random, "random.txt")

""" ARRAY OF ALL FETCHED ARTICLES URLS """
urls = read_file("examples.txt")
for link in read_file("known.txt"):
    urls.append(link)

""" PARSE AND SCORE ARTICLES """

result_list = []
for url in urls:
    try:
        scraped_html_content = scrape(url.strip(), settings.tags)
        text_content = tags_to_string(scraped_html_content)
        result = score(url.strip(), text_content, keywords_scoring)
        result_list.append(result)
    except Exception as e:
        print(e)

""" SAVE AS XLSX """
#df = pd.DataFrame([o.__dict__() for o in result_list])
#df.to_csv("C:\\Users\\42194\\Desktop\\TP\\WebScraper\\Files\\report.csv", encoding='utf-8-sig')
#print(df)

""" SEND TO ELASTIC """
add_article([o.__dict__() for o in result_list])
