from datetime import datetime
import os

def get_filename():
    timestamp = str(datetime.now().strftime("%d_%m_%Y_%H_%M"))
    return "report_" + str(timestamp) + ".csv"
