import csv


def write_to_csv(list_input):
    # The scraped info will be written to a CSV here.
    try:
        with open("dataSet.csv", "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen)
            csv_writer.writerow(list_input)
    except:
        return False
