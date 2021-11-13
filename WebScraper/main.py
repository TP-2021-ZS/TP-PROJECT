# This Python file uses the following encoding: utf-8
from Process.crawler import get_urls_known_source
from Process.crawler import get_urls_random_source
from Data.data_processor import write_array_to_file
from Data.data_processor import read_file
from Process.parser import scrape
from Process.parser import tags_to_string
from Process.score import score
from settings import settings
import pandas as pd

keywords = read_file(settings.keywords)
known_urls = read_file(settings.known_urls)

#articles_random = get_urls_random_source(50, keywords)
#articles_known = get_urls_known_source(known_urls, keywords)

#write_array_to_file(articles_random, "random.txt")
#write_array_to_file(articles_known, "known.txt")

urls = read_file("random.txt")
for link in read_file("known.txt"):
    urls.append(link)


result_list = []
for url in urls:
    try:
        scraped_html_content = scrape(url.strip(), settings.tags)
        text_content = tags_to_string(scraped_html_content)
        result = score(url.strip(), text_content, keywords)
        result_list.append(result)
    except Exception as e:
        print(e)


df = pd.DataFrame([o.__dict__() for o in result_list])
df.to_csv("C:\\Users\\42194\\Desktop\\7-semester\\TP\\WebScraper\\Files\\df.csv", encoding='utf-8-sig')
print(df)

