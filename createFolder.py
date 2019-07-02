import datetime
import os


def createFolder(folder):
    try:
        os.mkdir(folder)
    except:
        print(folder + "folder already exists. Please check the parent directory. ")


if __name__ == "__main__":
    root_path = "C:\\Users\\Joyel Manoj\\OneDrive - Drexel University\\Drexel\\Summer-2018_19"
    acct110 = root_path+"\\ACCT110"
    info605 = root_path+"\\INFO605"
    info710 = root_path+"\\INFO710"
    info712 = root_path+"\\INFO712"

    class_list = [acct110, info605, info710, info712]

    day = datetime.datetime.today().weekday()

    folder = "\\wk"
    week_number = 2

    if week_number <= 10 and day is 0:
        folder = folder + str(week_number)
        for directory in class_list:
            createFolder(directory + folder)
        week_number = week_number + 1
