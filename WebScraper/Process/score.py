import re
from Object.model_objects import ScoringResult


def score(url, content, keywords):
    final_score = 0
    for key in keywords:
        matches = re.findall(key.strip(), content.lower())
        final_score += len(matches)
    content_arr = re.split(" ", content)
    final_score = (final_score / len(content_arr)) * 100
    return ScoringResult(url, content, final_score)
