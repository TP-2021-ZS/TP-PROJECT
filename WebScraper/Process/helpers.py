from datetime import datetime, timedelta
import os

def get_filename():
    timestamp = str(datetime.now().strftime("%d_%m_%Y_%H_%M"))
    return "report_" + str(timestamp) + ".csv"


def get_date_after(range):
    if range == "day":
        date_after = datetime.today() - timedelta(days=1)
        return date_after.strftime("%Y-%m-%d")
    elif range == "week":
        date_after = datetime.today() - timedelta(days=7)
        return date_after.strftime("%Y-%m-%d")
    elif range == "month":
        date_after = datetime.today() - timedelta(days=30)
        return date_after.strftime("%Y-%m-%d")
    elif range == "year":
        date_after = datetime.today() - timedelta(days=365)
        return date_after.strftime("%Y-%m-%d")
    else:
        return 0


def check_reports_dir(project_path):
    if not os.path.isdir(project_path + "\\Reports\\"):
        os.mkdir(project_path + "\\Reports\\")


def check_logs_dir(project_path):
    if not os.path.isdir(project_path + "\\Logs\\"):
        os.mkdir(project_path + "\\Logs\\")
