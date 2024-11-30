import os
import time
import datetime
import sqlite3
import re

def get_sensors():
    sensors = []
    for filename in os.listdir("/sys/bus/w1/devices"):
            if re.match( r'\w{2}-\w{12}', filename ):
                sensors.append( filename )
    return sensors

#def read_temp_raw(device_file):
#    f = open(device_file, 'r')
#    lines = f.readlines()
#    f.close()
#    return lines

def read_temp_raw(device_file):
   with open(device_file) as dev_fh:
      return dev_fh.readlines()

def read_temp(sensor):
    device_file = '/sys/bus/w1/devices/' + sensor + '/w1_slave'
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect('hometemp.db')
cur = conn.cursor()

sensors = get_sensors()

for sensor in sensors:
    temp_f = read_temp(sensor)
    reading = ( sensor, current_time, temp_f )
    cur.execute( 'INSERT INTO readings( sensor, datetime, temperature) VALUES(?, ?, ?)', reading )
    conn.commit()