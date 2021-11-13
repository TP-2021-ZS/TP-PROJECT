import time
from googlesearch import search
from settings import settings


def get_urls_known_source(known_pages_list, keywords):
    urls_list = []
    print("<crawling_known_urls>")
    for page in known_pages_list:
        query = "site:" + page.strip() + " intitle:investícia"
        print("<crawling_page_" + str(page.strip()) + ">")
        for item in crawl(query, settings.get_urls_known):
            urls_list.append(item)

    return urls_list


def get_urls_random_source(n, keywords):
    print("<crawling_random_urls>")
    query = "intitle:investíciu"  # & after:2021-10-01 for datetime boundary

    return crawl(query, settings.get_urls_random)


def crawl(query, num_of_pages):
    urls_list = []

    try:
        for i in search(query, tld="sk", num=num_of_pages, stop=num_of_pages, pause=15):
            print("<appending_content>")
            urls_list.append(i)
    except Exception as e:
        print(e)
        time.sleep(2)

    return urls_list
