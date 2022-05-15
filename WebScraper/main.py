# This Python file uses the following encoding: utf-8
import logging

from Data.data_processor import *
from Process.crawler import get_urls_random_source
from Process.helpers import *
from Process.parser import *
from Process.score import score
from settings import settings

try:
    """CREATE PROJECT FILES"""
    check_reports_dir(project_path=settings.project_path)
    check_logs_dir(project_path=settings.project_path)

    """LOGGING ERRORS"""
    logging.basicConfig(filename=settings.project_path + '/Logs/runtime_errors.log', level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)

    """ INIT - read settings """
    scoring_dictionary = get_scoring_dict(settings.keywords_scoring)
    keywords_search_content = read_file(settings.keywords_search_content)
    keywords_search_title = read_file(settings.keywords_search_title)
    known_urls = read_file(settings.known_urls)
    blacklist_urls = read_file(settings.blacklist_urls)
    list_of_recipients = settings.list_of_recipients
    num_urls = settings.random_articles_per_query
    num_queries = settings.num_of_random_queries
    date_after = str(get_date_after(settings.date_after)).lower()
    project_path = settings.project_path

    """ GET ARTICLES URLS """
    #articles_known = get_urls_known_source(num_urls,
    #                                       num_queries,
    #                                       keywords_search_content,
    #                                       keywords_search_title,
    #                                       known_urls,
    #                                       blacklist_urls,
    #                                       date_after)
    articles_random = get_urls_random_source(num_urls,
                                             num_queries,
                                             keywords_search_content,
                                             keywords_search_title,
                                             blacklist_urls,
                                             date_after)

    """ PARSE AND SCORE *RANDOM* ARTICLES """
    #found_urls = articles_known + articles_random
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
    df.to_csv(project_path + "/Reports/" + filename, encoding='utf-8-sig')

    """ SEND TO ELASTIC """
    # add_article([o.__dict__() for o in result_list])

    """ SEND VIA EMAIL """
    # send_mail_report(list_of_recipients, filename)

except Exception as e:
    """LOGGING ERRORS"""
    logger.error(e)
