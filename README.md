# python-web-server
[WORK IN PROGRESS]

* Using Flask and Flask-API to run a webserver on Raspberry Pi using Python

```
sudo pip install Flask
sudo pip install Flask-API
```

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
