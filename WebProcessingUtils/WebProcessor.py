import nltk
import pandas as pd
from fuzzywuzzy import fuzz as fw

from WebProcessingUtils.WebScrubber import WebScrubber


class WebProcessor:
    def __init__(self, export_folder: str, export_format='xlsx'):
        self.scrubber = WebScrubber()
        self.export_folder = export_folder
        self.export_format = export_format

    def process_url(self, url) -> str:
        soup = self.scrubber.get_web_page_soup(url)

        # Obtain texts
        titles = self.scrubber.get_string_by_tags(soup, ['h1', 'title'])
        paragraphs = self.scrubber.get_string_by_tags(soup, ['p'])
        content = self.scrubber.get_string_by_tags(soup, ['h1', 'title', 'p'])

        # Create DataFrames
        dataframes = {
            'titles': self.__create_dataset(titles),
            'paragraphs': self.__create_dataset(paragraphs),
            'content': self.__create_dataset(content)
        }

        # Export DataFrames
        fn = self.__export(dataframes, url)
        print("Successfully processed: {}".format(url))
        return fn

    def __create_tokens(self, string: str) -> list:
        tokens = [t for t in string.split()]
        stopwords = ['z', 'zo', 'v', 'vo', 'za', 'do', 'popod', 'poza', 'ponad', 'okolo', 'dolu', 'dolem hore', 'vôkol',
                     'uprostred', 'vďaka', 'spoza', 'pomedzi', 'namiesto', 'bez', 'miesto', 'mimo', 'od', 'odo',
                     'okrem', 'prostred', 'spod', 'sponad', 'spomedzi', 'k', 'ku', 'kvôli', 'napriek', 'naproti',
                     'proti', 'voči', 'cez', 'medzi', 'na', 'nad', 'o', 'po', 'pod', 'popod', 'pre', 'pred', 'skrz',
                     'na', 'popri', 'pri', 's', 'so', 'nado', 'bez', 'bezo', 'mimo', 'a', 'i', 'ani', 'jednak', 'hneď',
                     'ako', 'aj', 'ba', 'dokonca', 'nielen', 'ale', 'avšak', 'však', 'síce', 'alebo', 'buď', 'veď',
                     'totiž', 'keďže', 'pretože', 'že', 'keďže', 'aby', 'až', 'takže', 'ak', 'keby', 'keď', 'síce',
                     'hoci', 'sotva', 'až', 'kým', 'akoby', 'keby', 'ako', 'tým', 'tak', 'ibaže', 'iba', 'by', 'tu',
                     'tam', 'či', 'čo', 'a', 'ty', 'on', 'ona', 'ono', 'my', 'vy', 'oni', 'ony', 'môj', 'tvoj',
                     'jeho/jej', 'náš', 'váš', 'ich', 'moje', 'tvoje', 'naše', 'vaše', 'moja', 'tvoja', 'naša', 'vaša',
                     'mojich', 'tvojich', 'vašich', 'našich', 'mojimi', 'tvojimi', 'vašimi', 'našimi', 'sem', 'sa',
                     'svoj', 'seba', 'tá', 'to', 'tento', 'toto', 'kto', 'čo', 'koho', 'čoho', 'komu', 'čomu', 'kým',
                     'čím', 'kde', 'kedy', 'týmito', 'hentí', 'hentá', 'henten', 'hento', 'nikto', 'nikde', 'každý',
                     'každí', 'sám', 'nič', 'každým', 'každom', 'každého', 'každými', 'každých', 'každopádne', 'niekto',
                     'niekde', 'mojej', 'tvojej', 'našej', 'vašej', 'mňa', 'ju', 'jeho', 'vás', 'ich', 'tých',
                     'tamtých', 'tamtie', 'tamtoho', 'nás', 'nami', 'tebou', 'tebe', 'nej', 'im', 'čím', 'čiou', 'tie',
                     'tí', 'ktorýsi', 'ktorási', 'ktorési', 'bez ktoréhosi', 'bez ktorejsi', 'ktoréhosi',
                     'dám ktorémusi', 'dám ktorejsi', 'dám ktorémusi', 'vidím ktorési', 'ktorúsi', 'ktorési',
                     'ktoromsi', 'ktorejsi', 'ktoromsi', 'ktorýmsi', 'ktorousi', 'ktorýmsi', 'kadejaký', 'kadejako',
                     'kadejakými', 'kadejakí', 'kadečo', 'kadečom', 'ktorísi', 'ktorési', 'ktorési', 'ktorýchsi',
                     'ktorýmisi', 'čísi', 'čiasi', 'čiesi', 'čiehosi', 'čejsi', 'čiehosi', 'čiemusi', 'čejsi',
                     'čiehosi', 'čiusi', 'čomsi', 'čísi', 'čiesi', 'číchsi', 'číchsi', 'čímisi', 'lenže', 'lebo', 'nuž',
                     'ostatne', 'aspoň', 'prosím', 'bodaj', 'by', 'azda', 'až', 'ešte', 'aj', 'dokopy', 'napríklad',
                     'asi', 'božechráň', 'sotva', 'áno', 'práve', 'jedine', 'jediná', 'jediný', 'jedinou', 'jediným',
                     'jedinými', 'jediných', 'ma', 'je', 'a', 'ach', 'jaj', 'joj', 'ó', 'au', 'fuj', 'haha', 'hehe',
                     'hihi', 'haló', 'aha', 'hej', 'hľa', 'pst', 'nate', 'hijo', 'ahoj', 'čau', 'pá', 'servus,zbohom',
                     'beda', 'mu', 'seba', 'sa', 'kto', 'čo', 'kde', 'ako', 'prečo', 'koľko', 'koľkonásobný', 'to',
                     'takto', 'vtedy', 'preto', 'toľko', 'toľkonásobný', 'niekto', 'voľačo', 'dakde', 'hocikam',
                     'sotvačo', 'málokedy', 'podaktorí', 'zriedkakedy', 'ktoviekam', 'komusi', 'akokoľvek', 'sotvaký',
                     'bohviekam', 'kadiaľ', 'bohviekadiaľ', 'máločo', 'málokde', 'istý', 'iný', 'taký', 'inakší',
                     'tamže', 'inde', 'inam', 'toľko', 'isto', 'inak', 'takže', 'ináč', 'všetci', 'všade', 'vždy',
                     'nikdy', 'všetko', 'každý', 'žiaden', 'nijako', 'ničí', 'sám', 'samý', 'samé', 'samého', 'samých',
                     'sami', 'čia', 'čohosi', 'si', 'sebou', 'sebe', 'ktorý', 'aký', 'ktorým', 'akým', 'ktorí', 'akí',
                     'ktorých', 'akých', 'ktorými', 'akými', 'istý', 'tým', 'istým', 'tí', 'istí', 'tých', 'istých',
                     'tými', 'istými', 'ten', 'tebe', 'teba', 'jemu', 'tomu', 'komusi', 'nikomu', 'nikom', 'nikoho',
                     'všetkým', 'všetkých', 'všetkými', 'viacerými', 'viacerých', 'čí', 'dačí', 'ničí', 'hocikde',
                     'kedysi', 'predtým', 'akému', 'takému', 'dajakému', 'nijakému', 'nijakým', 'dajakým', 'takým',
                     'nejako', 'niečo', 'toľko', 'ktoviekoľko', 'koľkokrát', 'toľkokrát', 'niekoľkokrát', 'nikdy',
                     'koľký', 'raz', 'toľký', 'niekoľký', 'niekoľká', 'niekoľké', 'nikoľkí', 'niekoľkými', 'niekoľkých',
                     'nikeoľkým', 'tade', 'tadiaľ', 'odtiaľ', 'odtadiaľ', 'potiaľ', 'potiaľto', 'žiadny', 'žiadna',
                     'žiadne', 'žiadnymi', 'žiadnym', 'žiadnej', 'žiadných', 'mi', 'ten', 'tento', 'tamten', 'onen',
                     'taký', 'onak', 'hentaký', 'hentakí', 'akiste', 'istotne', 'zrejme', 'určite', 'isto', 'naisto',
                     'bezpochyby', 'bezpochybne', 'hlavne', 'najmä', 'len', 'popravde', 'zvlášť', 'že', 'zasa', 'zas',
                     'zase', 'znova', 'znovu', 'žebože', 'žeby', 'žiaľ', 'ktorá', 'ktorej', 'ktorou', 'celkom', 'čisto',
                     'čoskoro', 'dobre', 'doslovne', 'fakticky', 'iste', 'jednako', 'jednoducho', 'konečne', 'menovite',
                     'najskorej', 'najskôr', 'nakoniec', 'koncu', 'naopak', 'napokon', 'napospol', 'nepochybne',
                     'nesporne', 'nevyhnutne', 'podobne', 'práve', 'priamo', 'proste', 'rovno', 'rozhodne', 'skoro',
                     'skôr', 'skutočne', 'určite', 'vcelku', 'vlastne', 'zvlášť', 'kdeže', 'potom', 'takisto',
                     'doslova', 'dočista', 'vskutku', 'bezmála', 'napodiv', 'podistým', 'preboha', 'takzvaný', 'tzv.',
                     'takzvaná', 'takzvané', 'takzvanými', 'takzvaných', 'takzvaným', 'takzvanej', 'takzvanému',
                     'takzvaného', 'takzvanú', 'inokedy', 'čomusi', 'dakto', 'dačo', 'dajaký', 'niečí', 'voľakto',
                     'ktokoľvek', 'razy', 'ktože', 'nadomnou', 'none', 'null', 'sú', 'už', 'eho', 'nie', 'jej']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        invalid_chars = ['"', '(', ')', '{', '}', '[', ']', '\'', '„', '“']

        # clean tokens
        clean_tokens = []
        for token in tokens:
            # Check for numbers -> translate to standard decimal format
            for n in numbers:
                if n in token:
                    token = token.replace(',', '')
                    break

            # Replace invalid chars
            for ic in invalid_chars:
                token = token.replace(ic, '')

            # Check for stop words
            if token not in stopwords:
                # Check for invalid information
                if len(token) > 1 and not ('$' in token or '€' in token or '%' in token or token.isdigit()):
                    clean_tokens.append(token)

        return clean_tokens

    def __create_dataset(self, string: str) -> pd.DataFrame:
        tokens = self.__create_tokens(string)

        # create DF
        df = []
        for key, val in nltk.FreqDist(tokens).items():
            sim = False
            for line in df:
                if line[0][0:3] == key[0:3] and fw.ratio(line[0],
                                                         key) >= 72:  # and fw.partial_ratio(line[0], key) >= 80:
                    line[1] += val
                    sim = True
                    break

            if not sim:
                df.append([key, val])

        df = pd.DataFrame(data=df, columns=['word', 'count'])
        df.sort_values(by='count', ascending=False, inplace=True)

        return df

    def __export(self, data_frames: dict, url: str) -> str:
        stripped_url = url.replace('https://', '').replace('wwww.', '').split('?')[0].split('/')
        file_name = "{}.{}".format(stripped_url[0] + ' - ' + stripped_url[-2], self.export_format)

        if self.export_format == 'xlsx':
            with pd.ExcelWriter(self.export_folder + file_name) as writer:
                for key, val in data_frames.items():
                    val.to_excel(writer, sheet_name=key, index=False)
        elif self.export_format == 'csv':
            for key, val in data_frames.items():
                val.to_csv("{} - {}".format(self.export_folder + file_name, key), index=False)
        else:
            raise ValueError("Incorrect export format.")

        return file_name
