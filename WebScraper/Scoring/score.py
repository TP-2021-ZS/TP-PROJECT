import re


def score(content, keywords):
    final_score = 0
    for key in keywords:
        matches = re.findall(key, content.lower())
        final_score += len(matches)

    return final_score
