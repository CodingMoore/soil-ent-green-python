import time
import Adafruit_ADS1x15
from datetime import datetime
import pyrebase
import envVar

dryValue = 2.23  #Calibration Value with sensor in Air (/10000)
wetValue = 1.09  #Calibration Value with sensor in Water (/10000)

config = {
  "apiKey": envVar.API_KEY,
  "authDomain": envVar.AUTH_DOMAIN,
  "databaseURL": envVar.DATABASE_URL,
  "storageBucket": envVar.STORAGE_BUCKET
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

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

    #"timestamp": {".sv": "timestamp"} read by firebase and converted into a SERVER timestamp.
    #"dateTime": datetime.now().strftime("%d/%m/%Y %H:%M:%S") creates a CLIENT date/time string with formatting.
    dataObject = {
      "timestamp": {".sv": "timestamp"},
      "dateTime": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
      "moisture": percent
    }

    print("Channel 0: {0}".format(dataObject))

    db.child("hardware").child("v001-L33t-p90X-t800").child("soilMoisture").child("latest").set(dataObject)
    db.child("hardware").child("v001-L33t-p90X-t800").child("soilMoisture").child("running").push(dataObject)

    time.sleep(3)


