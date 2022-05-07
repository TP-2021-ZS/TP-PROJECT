import random
import time
from googlesearch import search
import re


"""def get_urls_known_source(num_urls, num_queries, known_pages_list, blacklisted_urls, date):
    results = []
    print("<crawling_KNOWN_urls>")
    queries = build_queries(keywords_search, num_queries)
    for query in queries:
        for item in crawl(query, num_urls):
            if blacklist_check(blacklisted_urls, item):
                result.append(item)
    return result

    return results
"""


def get_urls_random_source(num_urls, num_queries,  kw_search_cont, kw_search_title, blacklisted_urls, date_after):
    result = []
    print("<crawling_RANDOM_urls>")
    queries = build_queries(kw_search_cont, kw_search_title, num_queries, date_after)
    for query in queries:
        for item in crawl(query, num_urls):
            if blacklist_check(blacklisted_urls, item):
                result.append(item)
    return result


def crawl(query, num_urls):
    urls_list = []

    try:
        for i in search(query, tld="sk", lang="sk", num=num_urls, stop=num_urls, pause=50,
                        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"):
            print("<appending_content>")
            urls_list.append(i)
    except Exception as e:
        print(e)

    return urls_list


def build_queries(kw_search_content, kw_search_title, num_queries, date_after):
    queries = []
    end_content = len(kw_search_content)
    end_title = len(kw_search_title)

    """ IN TITLE QUERIES """
    for i in range(0, num_queries//2):
        query = "intitle:" + kw_search_title[random.randrange(0, end_title)].strip() + ","\
                + kw_search_title[random.randrange(0, end_title)].strip() + " -file" + " after:" + date_after
        queries.append(query)

    """ IN TEXT QUERIES"""
    for i in range(0, num_queries//2):
        query = "intext:" + kw_search_content[random.randrange(0, end_content)].strip() + ","\
                + kw_search_content[random.randrange(0, end_content)].strip() +\
                "," + kw_search_content[random.randrange(0, end_content)].strip() + " -file" + " after:" + date_after
        queries.append(query)

    return queries


def blacklist_check(blacklisted_urls, url):
    for blk_url in blacklisted_urls:
        x = re.search(blk_url.strip(), url)
        if x is not None:
            return False
    return True
