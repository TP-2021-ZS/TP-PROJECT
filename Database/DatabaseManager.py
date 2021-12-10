from elasticsearch import Elasticsearch, helpers

class DatabaseManager:
    def __init__(self):
        self.db_client = Elasticsearch("http://localhost:9200")

    def add_doc_to_db(self,doc):
        try:
            helpers.bulk(self.db_client, doc)
            print("Succesfully saved document into db")
        except StopIteration:
            print("Error during saving document into db")
            return