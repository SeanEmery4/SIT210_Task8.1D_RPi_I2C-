## Project: Communicate with light intensity sensor over I2C
## Author: Sean Emery
## Date: 6/04/202
################## Code referenced to aid understanding:
## Title: by1750.py Source code
## Author: Pibits
## Date: 2016
## Code version: 1.0
## Availability: http://www.pibits.net/code/raspberry-pi-bh1750-light-sensor.php
##################

import smbus
import time

# set device address on raspberry pi as addr
addr = 0x23 # Default device I2C address
ONE_TIME_HIGH_RES_MODE = 0x20 # from data sheet, command for one time high res read

bus = smbus.SMBus(1)  # use I2C number 1 (GPIO02 & GPIO03)

# function to return lux value of data returned from sensor
def convertToLux(data):
    # convert 2 bytes of data into a decimal number
    return ((data[1] + (256 * data[0])) / 1.2)

# function to read light in on i2c and return as a number
def readLight():
    # us smbus to read i2c data at the address addr, with command for one time
    # high resolution mode and store returned value in data
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE)
    # return the value returned from convert to number
    return convertToLux(data)


while True:
    # read light level and store in light level
    light_level = readLight()
    
    # test light level to output if it is too dark, dark, medium, bright or too bring
    if light_level < 20:
        print("Too Dark")
    elif light_level < 45:
        print("Dark")
    elif light_level < 65:
        print ("Medium")
    elif light_level < 150:
        print("Bright")
    else:
        print("Too Bright")
        
    # wait for half a second
    time.sleep(0.5)
