from fuzzywuzzy import fuzz as fw
from pandas import DataFrame, read_excel, ExcelWriter


class DatasetUnifier:
    def __init__(self, folder):
        if not folder:
            self.folder = './'
        else:
            self.folder = folder

    def unify(self, files: list):
        unified = {
            'titles': DataFrame(),
            'paragraphs': DataFrame(),
            'content': DataFrame()
        }

        for file in files:
            file_name = "{}{}".format(self.folder, file)

            df = read_excel(io=file_name, sheet_name='titles')
            unified['titles'] = self.__add_data_frame(unified['titles'], df)

            df = read_excel(io=file_name, sheet_name='paragraphs')
            unified['paragraphs'] = self.__add_data_frame(unified['paragraphs'], df)

            df = read_excel(io=file_name, sheet_name='content')
            unified['content'] = self.__add_data_frame(unified['content'], df)

        self.__export(unified, 'unified.xlsx')

    def __add_data_frame(self, unified: DataFrame, new_data: DataFrame) -> DataFrame:
        for index, row in new_data.iterrows():
            match = False

            for i, r in unified.iterrows():
                if r[0][0:3] == row[0][0:3] and fw.ratio(r[0], row[0]) >= 72:
                    r[1] += row[1]
                    match = True
                    break

            if not match:
                unified = unified.append(row, ignore_index=True)
        return unified

    def __export(self, data_frames: dict, file_name: str):
        with ExcelWriter(self.folder + file_name) as writer:
            for key, val in data_frames.items():
                val.to_excel(writer, sheet_name=key, index=False)

        print("Unified data file: '{}' has been created in {}.".format(file_name, self.folder))
