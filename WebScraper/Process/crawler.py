import time
from googlesearch import search


def get_urls_known_source(known_pages_list, keywords):
    urls_list = []
    print("<crawling_known_urls>")
    for page in known_pages_list:
        query = "site:" + page.strip() + " intitle:investícia"
        print("<crawling_page_" + str(page.strip()) + ">")
        crawl(query, 2)

    return urls_list


def get_urls_random_source(n, keywords):
    urls_list = []
    print("<crawling_random_urls>")
    for i in range(0, n):
        query = "intitle:investícia"  # & after:2021-10-01 for datetime boundary
        crawl(query, 2)

    return urls_list


def crawl(query, num_of_pages):
    urls_list = []

    try:
        for i in search(query, tld="sk", num=num_of_pages, stop=num_of_pages, pause=5):
            print("<appending_content>")
            urls_list.append(i)
    except:
        print("Err. Too many requests 429")
        time.sleep(2)

    return urls_list
