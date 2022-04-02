import datetime
from dataclasses import dataclass
from hashlib import md5
from Data.data_processor import read_conf
from Data.data_processor import get_root_domain


@dataclass
class ScoringResult:
    """Class for keeping track of scoring results."""
    id: str
    url: str
    article: str
    root_domain: str
    timestamp: datetime.datetime
    score: int = 0

    def __init__(self, url: str, article: str, score: int = 0):
        self.id = md5(url.encode()).hexdigest()
        self.url = url
        self.article = article
        self.root_domain = get_root_domain(url)
        self.timestamp = datetime.datetime.now()
        self.score = score

    def __str__(self):
        return "URL: " + self.url + "\tScore: " + str(self.score)

    def __dict__(self):
        return {
            'id': self.id,
            'url': self.url,
            'root_domain': self.root_domain,
            'timestamp': self.timestamp,
            'score': self.score
        }


@dataclass
class ProjectSettings:
    """Class for program settings."""
    tags: list
    keywords_scoring: list
    keywords_search_content: list
    keywords_search_title: list
    known_urls: list
    blacklist_urls: list
    list_of_recipients: list
    date_after: str
    num_of_random_queries: int = 20
    random_articles_per_query: int = 3
    known_articles_per_query: int = 2

    def __init__(self, file: str):
        conf = read_conf(file)
        self.tags = conf['tags']
        self.keywords_scoring = conf['keywords_scoring']
        self.keywords_search_content = conf['keywords_search_content']
        self.keywords_search_title = conf['keywords_search_title']
        self.known_urls = conf['known_urls']
        self.blacklist_urls = conf['blacklist_urls']
        self.num_of_random_queries = conf['num_of_random_queries']
        self.random_articles_per_query = conf['random_articles_per_query']
        self.known_articles_per_query = conf['known_articles_per_query']
        self.date_after = conf['date_after']
        self.list_of_recipients = conf['list_of_recipients']
