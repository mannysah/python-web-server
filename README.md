# python-web-server
[WORK IN PROGRESS]

* Using Flask and Flask-API to run a webserver on Raspberry Pi using Python

## More Details:
```
sudo pip install Flask
sudo pip install flask-api
```

* Run python server.py from the directory you clone this project.
* The app starts at http://localhost:5000/
* To run Motor: http://localhost:5000/api/runMotor - For now this is a GET, i will change this to a POST soon.
 

## Contents of Project
* Add server.py -- This is where the definition of End points and what they do is. For now, all the functions are in the same code. Eventually, i need to move them into functions of their own.
* Add directory templates and add home.html and motor.html in this directory. These are html files used to render the page. Its work IN-PROGRESS.
* RESOLVED BUG: The time.sleep doesnt work when i start the Motor. 
    * The motor keeps running. 
    * The workaround is to stop the motor manually using the below code. 
        * I am using GPIO Pins 36, 38, 40 (In GPIO.BOARD Mode)
        * That means these are wiringPI PINS 27, 28, 29 
        * Using these pins to send a 0 (LOW to 27 and 29)
        * This will stop the motor

```
pi@raspberrypi:~ $ gpio write 27 0
pi@raspberrypi:~ $ gpio write 29 0
```
