import time
import Adafruit_ADS1x15
from datetime import datetime
import pyrebase
import envVar
import firebase_admin
from firebase_admin import credentials, firestore

#cred = credentials.Certificate("serviceAccountKey.json")


dryValue = 2.23  #Calibration Value with sensor in Air (/10000)
wetValue = 1.09  #Calibration Value with sensor in Water (/10000)

config = {
  "apiKey": envVar.API_KEY,
  "authDomain": envVar.AUTH_DOMAIN,
  "databaseURL": envVar.DATABASE_URL,
  "projectId": envVar.PROJECT_ID,
  "storageBucket": envVar.STORAGE_BUCKET,
  "messagingSenderId": envVar.MESSAGING_SENDER_ID,
  "appId": envVar.APP_ID 
}

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred)

firestore_db = firestore.client()

#firebase = pyrebase.initialize_app(config)
#db = firebase.database()

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
      #"timestamp": firestore.SERVER_TIMESTAMP,
      "dateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
      "moisture": percent,
      "machineName": "v001-L33t-p90X-t800"
    }

    print("Channel 0: {0}".format(dataObject))

    #WORKING VERSION!!!
    firestore_db.collection("hardware").add(dataObject)

    # 2 second delay between readings
    time.sleep(2)



