import serial
import datetime
import pandas as pd
from time import sleep

def parseGPS():
    """
    Connects to the serial port to read NMEA Data from the GPS Module.
    Only reads from the $GPRMC lines and if the connection is valid.
    """
    port="/dev/cu.usbmodem14201" #or whatever port works on the device !!
    # for mac: /dev/cu.usbmodem14201
    # for rpi zero: /dev/ttyAMA0

    gps = serial.Serial(port, baudrate=9600)
    
    while True:
        line = str(gps.readline()).strip('\n')
        data = line.split(",")
        if data[0] == "b'$GPRMC":

            # only accept valid data
            if data[2] == "A":

                # prepare to append
                with open("data/raw/position.csv", "a") as f_pos:
                    lat = data[3]
                    long = data[5]

                    neg_lat, neg_long = False, False

                    # decode and adjust for negatives
                    if data[4] == 'S':
                        neg_lat = True

                    decoded_lat = decode(lat, 'lat', neg_lat)

                    if data[6] == 'W':
                        neg_long = True

                    decoded_long = decode(long, 'long', neg_long)

                    # write time, lat, long to the file in csv format
                    now = datetime.datetime.now()
                    f_pos.write(str(now) + ", " + str(decoded_lat) + ", " + str(decoded_long) + "\n")
                    print(str(now) + ", " + str(decoded_lat) + ", " + str(decoded_long))

                    # sleep(2)

def decode(coord, type, neg):
    """
    Converts NMEA GPS measurements to the more common degree format
    """
    if type == "lat":
        deg = int(coord[:2])
        dec = float(coord[2:])
        dec_converted = dec / 60
        deg_to_use = deg + dec_converted
    else: # long
        deg = int(coord[:3])
        dec = float(coord[3:])
        dec_converted = dec / 60
        deg_to_use = deg + dec_converted  

    if neg == True:
        deg_to_use = deg_to_use * -1

    return deg_to_use

if __name__ == "__main__":
    parseGPS()