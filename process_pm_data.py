
import os
import csv
import pandas as pd
import datetime


def is_file_empty(file_name):
    """ Check if file is empty by reading first character in it"""
    # open ile in read mode
    with open(file_name, 'r') as read_obj:
        # read first character
        one_char = read_obj.read(1)
        # if not fetched then file is empty
        if not one_char:
           return True
    return False

def main(raw_file_in):
    # set up file to be read & appended to
    with open(raw_file_in, 'a+', encoding='UTF8') as f_out:
        writer = csv.writer(f_out)

        # only write the header if the csv is empty to begin with
        if is_file_empty('data/processed/airquality_data_to_use.csv'):
            header = ['timestamp', 'pm1_cf', 'pm25_cf', 'pm10_cf', 'pm1', 'pm25', 'pm10']
            writer.writerow(header)

        # get the raw data from the raspberry pi
        f_in = open("data/raw/airquality_data.csv","r")

        # read in the lines one by one
        lines = f_in.readlines()
        for line in lines:
            line = line.replace("\n","")
            line = line[27:-3].split("), (")

            # grab data 
            oldDateObject, pm1_cf, pm25_cf, pm10_cf, pm1, pm25, pm10  = line[0], line[1], line[2], line[3], line[4], line[5], line[6]
            
            # remove labels
            pm1_cf, pm25_cf, pm10_cf, pm1, pm25, pm10 = pm1_cf[10:], pm25_cf[11:], pm10_cf[11:], pm1[7:], pm25[8:], pm10[8:-1]
            
            # get date back into a datetime object
            dateLst = oldDateObject[18:-1].split(", ")
            year, month, day, hour, minute, second, microsecond = int(dateLst[0]), int(dateLst[1]), int(dateLst[2]), int(dateLst[3]), int(dateLst[4]), int(dateLst[5]), int(dateLst[6])
            newDateObject = datetime.datetime(year, month, day, hour, minute, second, microsecond)
            row = [newDateObject, pm1_cf, pm25_cf, pm10_cf, pm1, pm25, pm10]
            
            # add data to csv
            writer.writerow(row)

if __name__ == "__main__":
    raw_file_in = 'data/processed/airquality_data_to_use.csv'
    main(raw_file_in)