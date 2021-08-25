# Terrestrial Environmental Monitoring

A project begun in the summer of 2021, aiming to explore electronics, environmental data visualization, and web development! 

### End Goal:
An automated environmental monitoring device that has pre-programmed routes and sends data to the cloud via IoT interfaces.
### Current Status (8/25/2021):
Sensors collect data, but the process to send it to my local computer and visualize it on Flask webpage is completely manual (completed via SSH into the Pi).

![pm_size_comparison](https://user-images.githubusercontent.com/58823003/130871849-527dcd6d-d703-4c09-89e1-8eb08ddcc22f.png)

## Electronics
I used a RaspberryPi Zero connected to a Breadboard and portable powerbank. As for the environmental monitoring tools, I connected a GPS Module as well as a Particulate Matter sensor (PM10, PM2.5, & PM1). I sensors for other common air pollutants, but not the materials to connect them to the breadboard. 

I connected to the RPi headlessly over SSH, but am looking to acquire a monitor/keyboard/mouse set to connect easier.

## Data Acquisition
Both the GPS module and PM monitoring device send data through a serial port. See: `Air_quality_v2.py`
The data is read in as bytes and then processed into a csv file which will be sent to my local computer after it is done processing.

## Data Visualization
After many trials and errors with plotting packages, I settled on `ipyleaflet` for geographical plotting and `plotly` for interactive timeseries data. My main goal was to make the data as interactive and intuitive as possible because environmental monitoring is an incredible tool for communicating data such that community members can make informed decisions for their health!

## Web Development
For this project I used a Flask app deployed on Heroku. I am very comfortable working in Python (and am excited to learn some more JavaScript and CSS) so this was an easy choice for me.

