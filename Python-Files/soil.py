import time
import Adafruit_ADS1x15
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

dryValue = 0.000223
wetValue = 0.000109

# serviceAccountKey.json is not included in this repo for security reasons.  The README contains instructions for re-creating this file.
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred)

firestore_db = firestore.client()

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
    voltage = adc.get_last_result()
    percent = mapToPercent(voltage,dryValue,wetValue,0,100)

    dataObject = {
      "dateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "moisture": percent,
      "machineName": "v001-L33t-p90X-t800"
    }

    print("Channel 0: {0}".format(dataObject))

    firestore_db.collection("hardware").add(dataObject)

    # The argument passed into time.sleep() is the delay between sensor readings, in seconds.
    time.sleep(2)



