from machine import Pin, I2C


import time
import utime

#Global Variable
ledTick = 0
bh1750Tick = 0

# CONSTANT
# The address of the sensor on the I2C bus
'''
The sensor's I2C address is set to 0x23 and the measurement command(0x10)
is sent to the sensor. Then the code waits for 180 milliseconds
for the measurement to complete. Then 2 bytes of data is read from the sensor
and stored in data variable. Then the data is converted to lux by using
the formula given in the datasheet. 
'''
address = 0x23
def readBH1750():
    i2c.writeto(address, bytes([0x10]))
    data = i2c.readfrom(address, 2)
    light_intensity = (data[0] << 8 | data[1]) / 1.2
    return light_intensity

start_time = time.ticks_ms()

def millis():
    return time.ticks_ms() - start_time


print('Version: Read Data from BH1750 sensor and display on shell')

#setup Digital O/p
led = Pin(2, Pin.OUT)

#setup i2c devices
i2c = I2C(scl=Pin(22), sda=Pin(21))


while True:    
    if millis() >= ledTick:
        ledTick = millis()+1000
        led.value(not led.value())

    if millis() >= bh1750Tick:
        bh1750Tick = millis() + 10000
        
        lux = readBH1750()
        
        data_sensor_string = "Light Intensity (lux):{:.2f} lx".format(lux)
        print(data_sensor_string)       
          
        timestamp = utime.time()
        time_tuple = utime.localtime(timestamp)
        time_string = "{}-{:02d}-{:02d} {}:{}:{}".format(time_tuple[0],time_tuple[1],time_tuple[2],time_tuple[3],time_tuple[4],time_tuple[5])
        print(time_string)
       