import os
import csv
import pandas as pd
from datetime import datetime

def is_file_empty(file_name):
    """ 
    Check if file is empty by reading first character in it
    """
    # open ile in read mode
    with open(file_name, 'r') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
           return True
    return False

def get_last_timestamp():
    df = pd.DataFrame(pd.read_csv('data/processed/airquality_data_to_use.csv'))
    last_row = df.iloc[-1] 
    last_timestamp = last_row['timestamp']
    return last_timestamp

def main():
    # set up file to be read & appended to
    processed_file = 'data/processed/airquality_data_to_use.csv'

    with open(processed_file, 'a+', encoding='UTF8') as f_out:
        writer = csv.writer(f_out)

        # grab the last date in the old file to compare
        prev_file_last_timestamp = get_last_timestamp()
        print('prev last timestamp: ' + prev_file_last_timestamp)

        # only write the header if the csv is empty to begin with (should only happen once)
        if is_file_empty(processed_file):
            header = ['timestamp', 'pm1_cf', 'pm25_cf', 'pm10_cf', 'pm1', 'pm25', 'pm10']
            writer.writerow(header)

        # grab the raw data that was uploaded from the raspberry pi
        f_in = open("data/raw/airquality_data.csv","r")

        # read in the lines one by one
        lines = f_in.readlines()
        for line in lines:
            # don't work with empty lines
            # if len(line.strip()) != 0 :
            try:
                line = line.replace("\n","")
                line = line[27:-3].split("), (")

                unformattedDateObject, pm1_cf, pm25_cf, pm10_cf, pm1, pm25, pm10  = line[0], line[1], line[2], line[3], line[4], line[5], line[6]

                # remove labels
                pm1_cf, pm25_cf, pm10_cf, pm1, pm25, pm10 = pm1_cf[10:], pm25_cf[11:], pm10_cf[11:], pm1[7:], pm25[8:], pm10[8:-1]
                
                # get date back into a  datetime object
                dateLst = unformattedDateObject[18:-1].split(", ")
                year, month, day, hour, minute, second, microsecond = int(dateLst[0]), int(dateLst[1]), int(dateLst[2]), int(dateLst[3]), int(dateLst[4]), int(dateLst[5]), int(dateLst[6])
                newDateObject = datetime(year, month, day, hour, minute, second, microsecond)

                # don't rewrite existing data, only append new data
                if newDateObject < datetime.strptime(prev_file_last_timestamp, '%Y-%m-%d %H:%M:%S.%f'):
                    continue

                row = [newDateObject, pm1_cf, pm25_cf, pm10_cf, pm1, pm25, pm10]
                print(row)
            
                #add data to csv
                writer.writerow(row)
            except IndexError:
                continue


if __name__ == "__main__":
    # raw_file_in = 'data/raw/airquality_data.csv'
    # main()
    # get_last_timestamp()
    main()
