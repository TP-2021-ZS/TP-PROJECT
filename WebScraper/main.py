# This Python file uses the following encoding: utf-8
#from Process.crawler import get_urls_known_source
from Process.crawler import get_urls_random_source
from Process.elastic import add_article
from Data.data_processor import write_array_to_file
from Data.data_processor import get_root_domain
from Data.data_processor import read_file
from Data.data_processor import get_scoring_dict
from Process.parser import scrape
from Process.parser import tags_to_string
from Process.score import score
from settings import settings
import pandas as pd
from Process.mail import send_mail_report
from Process.helpers import get_filename


""" INIT - read settings """
scoring_dictionary = get_scoring_dict(settings.keywords_scoring)
keywords_search_content = read_file(settings.keywords_search_content)
keywords_search_title = read_file(settings.keywords_search_title)
known_urls = read_file(settings.known_urls)
blacklist_urls = read_file(settings.blacklist_urls)
list_of_recipients = settings.list_of_recipients
num_urls = settings.random_articles_per_query
num_queries = settings.num_of_random_queries
date_after = settings.date_after

""" GET ARTICLES URLS """
#articles_known = get_urls_known_source(settings.get_urls_known, known_urls, keywords_search)
articles_random = get_urls_random_source(num_urls,
                                         num_queries,
                                         keywords_search_content,
                                         keywords_search_title,
                                         blacklist_urls,
                                         date_after)

""" ARRAY OF ALL FETCHED ARTICLES URLS """
#urls = read_file("examples.txt")

""" PARSE AND SCORE *RANDOM* ARTICLES """
result_list = []
for url in articles_random:
    try:
        scraped_html_content = scrape(url.strip(), settings.tags)
        text_content = tags_to_string(scraped_html_content)
        result = score(url.strip(), text_content, scoring_dictionary)
        result_list.append(result)
    except Exception as e:
        print(e)

""" SAVE AS CSV """
filename = get_filename()
df = pd.DataFrame([o.__dict__() for o in result_list])
df = df.sort_values('score', ascending=False)
df.to_csv("C:\\Users\\42194\\Desktop\\TP\\WebScraper\\Reports\\" + filename, encoding='utf-8-sig')
print(df)

""" SEND TO ELASTIC """
#add_article([o.__dict__() for o in result_list])

""" SEND VIA EMAIL """
send_mail_report(list_of_recipients, "report_02_04_2022_16_05.csv")
