from dataclasses import dataclass
from Data.data_processor import read_conf


@dataclass
class ScoringResult:
    """Class for keeping track of scoring results."""
    url: str
    article: str
    score: int = 0

    def __init__(self, url: str, article: str, score: int = 0):
        self.url = url
        self.article = article
        self.score = score

    def __str__(self):
        return "URL: " + self.url + "\tScore: " + str(self.score)

    def __dict__(self):
        return {
            'url': self.url,
            'article': self.article,
            'score': self.score
        }


@dataclass
class ProjectSettings:
    """Class for program settings."""
    tags: list
    keywords: list
    known_urls: list
    blacklist_urls: list
    date_after: str
    get_urls_random: int = 0
    get_urls_known: int = 0
    top_articles_num: int = 20

    def __init__(self, file: str):
        conf = read_conf(file)
        self.tags = conf['tags']
        self.keywords = conf['keywords']
        self.known_urls = conf['known_urls']
        self.blacklist_urls = conf['blacklist_urls']
        self.date_after = conf['date_after']
        self.get_urls_random = conf['get_urls_random']
        self.get_urls_known = conf['get_urls_known']
        self.top_articles_num = conf['top_articles_num']
