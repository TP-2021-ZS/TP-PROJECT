from dataclasses import dataclass


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
