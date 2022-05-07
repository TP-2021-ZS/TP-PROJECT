import re
from Object.model_objects import ScoringResult


def score(url, content, keywords):
    final_score = 0
    for key, value in keywords.items():
        matches = re.findall(key, content.lower())
        final_score += len(matches) * int(value)
    content_arr = re.split(" ", content)
    final_score = int((final_score / len(content_arr)) * 100)
    print("<Article_scoring_end>")
    return ScoringResult(url, content, final_score)
