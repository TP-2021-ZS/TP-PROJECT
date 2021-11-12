import csv


def write_to_csv(list_input):
    # The scraped info will be written to a CSV here.
    try:
        with open("dataSet.csv", "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen)
            csv_writer.writerow(list_input)
    except:
        return False


def read_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        Lines = file.readlines()

        return Lines
    except:
        return False


def write_array_to_file(array, filename):
    with open(filename, mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(array))
