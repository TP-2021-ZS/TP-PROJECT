import re
from Object.model_objects import ScoringResult


def score(url, content, keywords):
    final_score = 0
    for key in keywords:
        matches = re.findall(key.strip(), content.lower())
        final_score += len(matches)

    return ScoringResult(url, content, final_score)
