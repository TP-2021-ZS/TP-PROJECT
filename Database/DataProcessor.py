from Database.DatabaseManager import DatabaseManager
class DataProccessor:
    def __init__(self):
        self.report_keys = ["word", "count"]
        self.article_keys = ["url", "score"]
        self.db = DatabaseManager()

    def filter_keys(self,document, keys):
        return {key: document[key] for key in keys}

    def doc_generator_articles(self,df, keys):
        df_iter = df.iterrows()
        for index, document in df_iter:
            try:
                yield {
                    "_index": "articles",
                    "_type": "_doc",
                    "_id": f"{document['url']}",
                    "_source": self.filter_keys(document, keys),
                }
            except StopIteration:
                return

    def doc_generator_reports(self,df, sheet, keys):
        df_iter = df.iterrows()
        for index, document in df_iter:
            try:
                yield {
                    "_index": "report-" + sheet,
                    "_type": "_doc",
                    "_id": f"{document['word']}",
                    "_source": self.filter_keys(document, keys),
                }
            except StopIteration:
                return
    def prepare_and_save_docs(self,reports:{}, articles_df):
        articles = self.doc_generator_articles(articles_df, self.article_keys)
        titles = self.doc_generator_reports(reports.get("titles"), "titles", self.report_keys)
        paragraphs = self.doc_generator_reports(reports.get("paragraphs"), "paragraphs", self.report_keys)
        content = self.doc_generator_reports(reports.get("content"), "content", self.report_keys)
        self.db.add_doc_to_db(articles)
        self.db.add_doc_to_db(titles)
        self.db.add_doc_to_db(paragraphs)
        self.db.add_doc_to_db(content)