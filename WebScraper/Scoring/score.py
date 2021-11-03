import re

keywords = ['Tesla']


def score(content):
    final_score = 0
    for key in keywords:
        x = re.findall(key, str(content))
        final_score += len(x)

    return final_score
