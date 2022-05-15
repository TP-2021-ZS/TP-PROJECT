from elasticsearch import Elasticsearch


def add_article(list_articles):
    print("<Sending_to_elasticsearch>")
    es = Elasticsearch()
    for item in list_articles:
        res = es.index(index="articles", document=item)
    print("Upload to elastic status : " + res['result'])
