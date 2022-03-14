import random
import time
from googlesearch import search
import re


def get_urls_known_source(num_urls, known_pages_list, keywords, date):
    urls_list = []
    print("<crawling_KNOWN_urls>")
    for page in known_pages_list:
        query = "site:" + page.strip() + " intitle:investícia"
        print("<crawling_page_" + str(page.strip()) + ">")
        for item in crawl(query, num_urls):
            urls_list.append(item)

    return urls_list


def get_urls_random_source(num_urls, keywords_search, blacklisted_urls):
    result = []
    print("<crawling_RANDOM_urls>")
    queries = build_queries(keywords_search)
    for query in queries:
        for item in crawl(query, num_urls):
            if blacklist_check(blacklisted_urls, item):
                result.append(item)
    return result


def crawl(query, num_of_articles):
    urls_list = []

    try:
        for i in search(query, tld="sk", lang="sk", tbs="qdr:d", num=3, stop=3, pause=50,
                        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"):
            print("<appending_content>")
            urls_list.append(i)
    except Exception as e:
        print(e)

    return urls_list


def build_queries(keywords_search):
    queries = []
    end = len(keywords_search)

    """ IN TITLE QUERIES """
    for i in range(0, 10):
        query = "intitle:" + keywords_search[random.randrange(0, end)].strip() + ","\
                + keywords_search[random.randrange(0, end)].strip() + " -file"
        queries.append(query)

    """ IN TEXT QUERIES"""
    for i in range(0, 10):
        query = "intext:" + keywords_search[random.randrange(0, end)].strip() + ","\
                + keywords_search[random.randrange(0, end)].strip() +\
                "," + keywords_search[random.randrange(0, end)].strip() + " -file"
        queries.append(query)

    return queries


def blacklist_check(blacklisted_urls, url):
    for blk_url in blacklisted_urls:
        x = re.search(blk_url.strip(), url)
        if x is not None:
            return False
    return True
