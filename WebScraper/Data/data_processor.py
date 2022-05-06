import csv
import json
import pandas as pd
import publicsuffix2
from urllib.parse import urlparse


def get_scoring_dict(filename):
    return pd.read_csv(filename, header=0, index_col=0).squeeze("columns").to_dict()


def save_results_to_csv(results_list):
    # The scraped info will be written to a CSV here.
    try:
        with open("dataSet.csv", "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen)
            csv_writer.writerow(results_list)
    except:
        return False


def read_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        Lines = file.readlines()

        return Lines
    except Exception as e:
        print(e)
        return False


def write_array_to_file(array, filename):
    with open(filename, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(array))


def read_conf(file):
    f = open(file, "r")
    settings_dict = json.loads(f.read())
    return settings_dict


def get_root_domain(url):
    psl = publicsuffix2.fetch()
    hostname = urlparse(url).hostname
    return publicsuffix2.get_public_suffix(hostname, psl)
