from Process.crawler import get_urls_known_source
from Process.crawler import get_urls_random_source
from Data.data_processor import write_array_to_file
from Data.data_processor import read_file
from Process.parser import scrape
from Process.parser import tags_to_string


TAGS = ['p', 'h1', 'h2', 'h3']
urls = read_file('urls.txt')
keywords = read_file('keywords.txt')


write_array_to_file(get_urls_known_source(urls, keywords), "known.txt")
write_array_to_file(get_urls_random_source(20, keywords), "random.txt")


#scraped_html_content = scrape(urls[0], TAGS)
#text_content = tags_to_string(scraped_html_content)


# article_score = score(text_content, keywords)
# print(article_score)