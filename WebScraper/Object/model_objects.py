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
    keywords_search: list
    known_urls: list
    blacklist_urls: list
    time_range_of_search: str
    get_urls_random: int = 0
    get_urls_known: int = 0
    top_articles_num: int = 20

    def __init__(self, file: str):
        conf = read_conf(file)
        self.tags = conf['tags']
        self.keywords_scoring = conf['keywords_scoring']
        self.keywords_search = conf['keywords_search']
        self.known_urls = conf['known_urls']
        self.blacklist_urls = conf['blacklist_urls']
        self.time_range_of_search = conf['time_range_of_search']
        self.get_urls_random = conf['get_urls_random']
        self.get_urls_known = conf['get_urls_known']
        self.top_articles_num = conf['top_articles_num']
