import nltk
import pandas as pd
from WebProcessingUtils.WebScrubber import WebScrubber


class WebProcessor:
    def __init__(self, export_folder: str, export_format='xlsx'):
        self.scrubber = WebScrubber()
        self.export_folder = export_folder
        self.export_format = export_format

    def process_url(self, url) -> None:
        soup = self.scrubber.get_web_page_soup(url)

        # Obtain texts
        titles = self.scrubber.get_string_by_tags(soup, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title'])
        paragraphs = self.scrubber.get_string_by_tags(soup, ['p'])
        content = self.scrubber.get_string_by_tags(soup, ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'title', 'p'])

        # Create DataFrames
        dataframes = {
            'titles': self.__create_dataset(titles),
            'paragraphs': self.__create_dataset(paragraphs),
            'content': self.__create_dataset(content)
        }

        # Export DataFrames
        self.__export(dataframes, url)
        print("Successfully processed: {}".format(url))

    def __create_tokens(self, string: str) -> list:
        tokens = [t for t in string.split()]
        stopwords = ['a', 'sa', 'si', 'ale', 'alebo', 'u', 'aj', 'lebo', 'na', 'o', 'v', 'pri', 'za', 'pred', 's', 'so',
                     'od', 'do']

        # clean tokens
        clean_tokens = []
        for token in tokens:
            if token not in stopwords:
                clean_tokens.append(token)

        return clean_tokens

    def __create_dataset(self, string: str) -> pd.DataFrame:
        tokens = self.__create_tokens(string)

        # create DF
        df = []
        for key, val in nltk.FreqDist(tokens).items():
            df.append([key, val])

        df = pd.DataFrame(data=df, columns=['word', 'count'])
        df.sort_values(by='count', ascending=False, inplace=True)

        return df

    def __export(self, data_frames: dict, url: str) -> None:
        stripped_url = url.replace('https://', '').replace('wwww.', '').split('?')[0].split('/')
        file_name = "{}{}.{}".format(self.export_folder, stripped_url[0] + ' - ' + stripped_url[-2], self.export_format)

        if self.export_format == 'xlsx':
            with pd.ExcelWriter(file_name) as writer:
                for key, val in data_frames.items():
                    val.to_excel(writer, sheet_name=key, index=False)
        elif self.export_format == 'csv':
            for key, val in data_frames.items():
                val.to_csv("{} - {}".format(file_name, key), index=False)
        else:
            raise ValueError("Incorrect export format.")

