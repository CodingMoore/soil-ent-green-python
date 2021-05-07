# **Soil-Ent-Green**
Project Initiated: 2021-03-05<br/>
Updated: 2021-03-17

__This repo is the Python (Raspberry Pi) side of this project. The JavaScript/React side of this project can be found in its own repo, [HERE](https://github.com/CodingMoore/soil-ent-green-react-v2).__ 
<br/>

__A Firestore database is also required for full functionality__

__Please install and set up the React app and the Firebase database before continuing with the Python/Raspberry Pi setup. There are instructions for doing both of these things inside the React app README.__

<br/>

## **Project Description**

<br/>

__Save Lives!__

Are you a terrible plant parent?  Does your “green” thumb spread death to all potted life-forms? Despair not, for now you have “Soil-Ent-Green”!

Soil-Ent-Green is a web/hardware application that allows users to remotely gather soil moisture data from their houseplants, and have that data graphed for them in real-time. 

A "Raspberry Pi" running the Soil-Ent-Green Python application is used to gather the data and send it to "Firestore" (NoSQL online database) for storage.  The Soil-Ent-Green React application retrieves the data from Firestore and provides a browser-based user interface. 

The React application has full C.R.U.D. capabilities and utilizes Firebase Authentication, so a user can only access, add, edit, and delete their own plants and database data.  As plant information is stored in the Firestore database with the sensor data, this application could be utilized by the user from any browser/device (if the application were deployed).

The Python application can be modified to account for individual sensor calibration and to adjust the interval between sensor readings.  For the purposes of quick demos and easy sensor calibration, this interval is set to 2 seconds by default.

<br/>

## **Project Explanation**

Soil-Ent-Green is an exercise/experiment in figuring out how a hardware product might be paired with its web app, without the user being required to edit any code. 

If this were a "real" product, custom hardware would be used instead of a Raspberry Pi, and it would come factory programmed with a unique "Machine Name" and database authentication key. The "Machine Name" would be printed on the hardware's exterior so that a user can easily find it and type it into the plant creation form in the React app.  



<br/>

## **Required for Use (Combined React and Python apps)**
* A browser that can run HTML5.
* A Firestore account/database.
* The React App found [HERE](https://github.com/CodingMoore/soil-ent-green-react-v2).
* [Node.js](https://nodejs.org/en/)
* A "Raspberry Pi" running "[Raspberry Pi OS](https://www.raspberrypi.org/software/)", and this Soil-Ent-Green Python 3 application.
* Capacitive soil moisture sensor.
* Analog to digital converter (ADC ADS1115 based).

<br/>

## **Raspberry Pi Setup**

1) Connect power, keyboard, mouse, and monitor to your raspberry pi.

2) Use the instructions [HERE](https://www.raspberrypi.org/software/) to install the Raspberry Pi Operating System.

3) Connect your Pi to the internet via ethernet cable or wi-fi.

4) Turn on your Raspberry Pi's 'I2C' ports by first opening the Pi's main menu, then selecting "Preferences", and then "Raspberry Pi Configuration". Click on the "Interfaces" tab, and enable "I2C". Click "Ok" and reboot the Pi. 

5) Open a Raspberry Pi terminal and type the following commands...

    <code>sudo apt-get update</code>

    <code>sudo apt-get install -y python-smbus i2c-tools</code>

6) Shut down your Pi, and disconnect power.

7) Connect your analog to digital converter to one of the I2C ports on your Pi, and then connect your capacitive moisture sensor to the analog to digital converter.

All of the previous steps, including additional troubleshooting step can be found [HERE](https://www.raspberrypi-spy.co.uk/2014/11/enabling-the-i2c-interface-on-the-raspberry-pi/).

8) Turn on your Pi, open a terminal, and enter the following commands...

    <code>sudo apt-get update</code>

    <code>sudo apt-get install build-essential python-dev python-smbus git</code>

    <code>sudo pip3 install Adafruit-ADS1x15</code>

    <code>sudo python3 setup&period;py install</code>

    <code>sudo pip3 install numpy</code>

    <code>sudo pip3 install firebase-admin</code>

9) Restart your Pi

<br/>

## **Application Installation and Setup Instructions**
<br/>
1) Copy and paste the following GitHub project link into your web browser's url bar and hit enter/return. 
<br/>

    https://github.com/CodingMoore/soil-ent-green-python

2) Download a .zip copy the repository by clicking on the large green "Code" button near the upper right corner of the screen.

3) Copy this zip file to your raspberry Pi's desktop.

4) Make a "projects" folder in the "__/home/pi__" directory of your Raspberry Pi.

5) Right click the .zip file and extract (unzip) it's contents.

6) Move the unzipped "__soil-ent-green-Python__" file into your "__/home/pi/projects__" folder.

7) Open "soil&period;py" file found in __/home/pi/projects/soil-ent-green-python/Python-Files__.  Find the following code at the bottom of the file and replace the number in the parenthesis with your desired sensor reading interval. This number represents the interval between readings in seconds.  For the purposes of quick demos and easy sensor calibration, it is set by default to 2 seconds.  For actual use, you would probably want the value to be some number of hours between readings.

```
time.sleep(2)
```

8) If you scroll up slightly from the bottom of the file, you will see the following code..

```
dataObject= {
  "dateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
  "moisture": percent,
  "machineName: "v001-L33t-p90X-t800"
}
```

  The value __v001-L33t-p90X-t800__ inside of the quotation marks is the Machine Name.  You write this down carefully, as you will need to enter this string exactly when adding a plant to the React App.  You are free to change this string to anything, so what you enter into the React App and the "soil&period;py" __dataObject__ value are the same.

<br/>

## **Create a serviceAccountKey.json File**
<br/>

__Before creating your serviceAccountKey.json file, make sure to push this project to your github account.  If you do not, you risk accidentally exposing your secret account information to the world.__

You should have already set up your Firestore database using the instructions found in the Soil-Ent-Green React application README.  If you have not done this, please do so now.  The React application can be found [HERE](https://github.com/CodingMoore/soil-ent-green-react-v2).

1) Go to your Firestore project and click on the gear icon next to "Project Overview", and then click on "Project Settings". Click on the "Service Accounts" tab.

2) Click on the "Generate new private key" Button. Then click on the "Generate key" button. A new file should automatically be downloaded to your pi's default downloads folder.

__Your private key gives access to your project's Firebase services. Keep it confidential and never store it in a public repository. Store this file securely, because your new key can't be recovered if lost.__

3)  Rename this file "__serviceAccountKey.json__" and move it to __/home/pi/projects/soil-ent-green-python/Python-Files__

<br/>

## **Running the Application**

<br/>

<hr/>

### __Warning:__ Once the Python/Raspberry Pi application has been started, it will continue to send data to Firestore at the "__time.sleep()__" interval that you have set in the "__soil&period;py__" file  (default: 2 seconds).  It will do so until the application is stopped, or the Pi is shut down. Viewing a live data graph in the React app will also count toward your read/write limits whenever new data points appear.

<br/>

### If your "__time.sleep()__" interval is low, and/or you forget to turn it off the application, __you could go beyond Firestore's threshold for FREE database read/writes or storage.__  As of the time of this writing, Firestore's "Spark" plan will not charge you when this threshold is reached, but the application will cease to function until data is deleted, or when the read/write threshold resets the next day.  However if you are not using the "Spark" plan, this could potentially cost you money.

<br/>

### I will not be held responsible in any way shape or form for any damages or costs that you incur while using these applications or by following my instructions.  To track your Firestore Read/Write usage, go to your projects Firestore and select the "Usage" tab.  To check your "plan" type, you can then click on "View in Usage and Billing", and then on the "Details & settings" tab.
<hr/>

<br/>

Open a terminal on the Pi and navigate to /home/pi/projects/soil-ent-green-python/Python-Files.  When you are ready to begin running the application and begin sending data to Firestore, you can type the following commands to start and stop the application...

<br/>

To Start:  <code>sudo python3 soil&period;py</code>

### To Stop: __ctrl+c__
<br/>

When the application starts, you should see the following message in the terminal:

"__Readout of Soil Moisture Data Begins Now__"

If you log into the React application and click on the plant that you have created using the "Machine Name" found in the soil&period;py file, a live graph of the moisture data should be generated.

<br/>

## __Sensor Calibration__

Once you are getting readings in the Pi's terminal from your sensor, you can calibrate it. "Sensor Value" should appear in the terminal ever time a sensor reading is made.  When taking the following sensor readings, allow the values to stabilize over a few seconds before writing them down.

1) With the sensor completely dry, and dangling in the air (do not hold it directly), write down the Sensor Value.  This will be your "dryValue".

2) Dip the sensor in a class of water to just __BELOW__ the white line, __BELOW__ the sensor circuitry.  Do not get the sensor wet above this line.  Steps can be taken to waterproof the sensor, but are not covered here.  Write down the Sensor Value.  This will be your "wetValue".

3) Shut down the application by typing __ctrl+c__ in the terminal.

4) Change the "wetValue" and "dryValue" numbers at the top of the soil&period;py file with the values you just got from your calibration testing. It is normal for these values to be large.  For example, __dryValue = 22300__, __wetValue = 10900__

5) Save the soil&period;py file

<br/>

## **Known Bugs / Planned Updates**
* Every data reading that is sent to Firestore currently creates a new document.  In the future, this will be modified so that many sensor readings will be placed in the same document, making read, writes, and deletes more efficient.

* The application currently needs to be started and stopped via terminal command.  In the future, this will be done by other means (through the React App or physical button?).

<br/>

## **Technology Used (Combined React and Python apps)**
__Hardware:__<br/>
* [Raspberry Pi 3B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) <br/>
* SwitchDoc [Capacitive Plant Moisture Sensor](https://shop.switchdoc.com/products/capacitive-plant-moisture-sensor-grove?pr_prod_strat=copurchase&pr_rec_pid=1447107919916&pr_ref_pid=229332680734&pr_seq=uniform) Corrosion Resistant Grove<br/>
* SwitchDoc [Grove ADC](https://shop.switchdoc.com/products/grove-4-channel-16-bit-analog-to-digital-converter?pr_prod_strat=copurchase&pr_rec_pid=229332680734&pr_ref_pid=229338251294&pr_seq=uniform) - 4 Channel 16 Bit Analog to Digital Converter (based on ADS1115)<br/>
* SwitchDoc [Pi2Grover](https://shop.switchdoc.com/collections/sensors/products/pi2grover-raspberry-pi-to-grove-connector-interface-board) - Raspberry Pi to Grove Connector Interface Board.<br/>
* SwitchDoc [Grove Cable](https://shop.switchdoc.com/products/grove-30cm-universal-4-pin-5-pack?_pos=1&_sid=2bb98f7db&_ss=r) - 30cm Universal 4-pin: 5-pack

__Software:__<br/>
* Python 3<br/>
* React.js<br/>
* JavaScript<br/>
* Node.js<br/>
* CSS<br/>
* Bootstrap<br/>
* Firebase (Firestore) database

<br/>

## **Authors and Contributors**
Authored by: Randel Moore

<br/>

## **Contact**
CodingMoore@gmail.com

<br/>

## **License**

GPLv3

Copyright © 2021 Randel Moore

