#!/usr/bin/env python
#-*- coding: utf-8 -*-
import time
import serial
import datetime
import sys
from flask import Blueprint
import RPi.GPIO as GPIO
import models.Coordinates as Coordinates

BAUD = 9600
PORT = '/dev/ttyACM0'
bp = Blueprint('gps', __name__, url_prefix='/gps')

@bp.route('/coordinates',methods=["GET"])
def readCordinates():
    ser = serial.Serial(PORT, BAUD, timeout = 5)
    if(ser.isOpen() == False):
        ser.open()
    while True:
        line = ser.readline()
        if line.startswith( '$GPGGA' ) :
            try :
              time, lat, _, lon = line.strip().split(',')[1:5] # move inside `try` just in case...
              lat = float( lat )
              lon = float( lon )
              print lat
              print lon
              eventtime = datetime.datetime.fromtimestamp(int(float(time))).strftime('%B-%Y-%d %H:%M:%S')
              GPIO.cleanup()
              return Coordinates(lat, lon, time)
            except ValueError as e:
                print e