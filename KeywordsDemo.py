import pandas as pd
from Database.DataProcessor import DataProccessor
from WebProcessingUtils.WebProcessor import WebProcessor

processor = WebProcessor('./exports/', 'xlsx')

processor.process_url("https://akcie.sk/tesla-predbehla-facebook-a-prekonala-trhovu-hodnotu-1-biliona/")

data_processor = DataProccessor()
# tuto som ulozila tie dataframy aby sa nemuseli nacitavat z file
reports = processor.dataframes

# tuto je to z csv ale ked sa to mergne s marekovym kodom tak sa posle rovno dataframe
articles = pd.read_csv('exports/articles-scoring.csv')
data_processor.prepare_and_save_docs(reports, articles)