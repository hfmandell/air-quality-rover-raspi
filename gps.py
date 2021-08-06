import serial
import datetime

port="/dev/cu.usbmodem14201"
gps = serial.Serial(port, baudrate=9600)

print(gps)

while True:
    line = str(gps.readline()).strip('\n')
    data = line.split(",")
    if data[0] == "b'$GPRMC":
        # only accept valid data
        if data[2] == "A":
            with open("position.txt", "a") as f_pos:
                # only print lat & long
                now = datetime.datetime.now()
                f_pos.write(str(now) + ", " + data[3] + ", " + data[5] + "\n")
                print(str(now) + ", " + data[3] + ", " + data[5])