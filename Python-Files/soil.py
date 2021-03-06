import time
import Adafruit_ADS1x15
from datetime import datetime

dryValue = 2.23  #Calibration Value with sensor in Air (/10000)
wetValue = 1.09  #Calibration Value with sensor in Water (/10000)

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

def mapToPercent(x,a,b,c,d):
    if x>a:
        return 0
    if x<b:
        return 100
    y = (x-a)/(b-a)*(d-c)+c
    return round(y)

adc.start_adc(0, gain=GAIN)

print("Readout of Soil Moisture Data Begins Now")

while True:
    value = adc.get_last_result()
    voltage = value/10000
    
    percent = mapToPercent(voltage,dryValue,wetValue,0,100)

    dataObject = {
      "dateTime": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
      "moisture": percent
    }

    print("Channel 0: {0}".format(dataObject))

    #print("Channel 0: {0}".format(percent))
    time.sleep(3)
