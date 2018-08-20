from flask import render_template
from flask import request
from flask_api import FlaskAPI
import RPi.GPIO as GPIO
import time

MOTORPINS = {"pin1A": 36, "pin1B": 38, "pin1E":40}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTORPINS["pin1A"], GPIO.OUT)
GPIO.setup(MOTORPINS["pin1B"], GPIO.OUT)
GPIO.setup(MOTORPINS["pin1E"], GPIO.OUT)

app = FlaskAPI(__name__)


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/api/runMotor',methods=["GET"])
def runMotor():
    """
    This function runs the Motor
    :return:        the rendered template 'home.html'
    """
    
    print "Inside run motor on"
    try:
        print "Turning motor on"
        GPIO.output(MOTORPINS["pin1A"],GPIO.HIGH)
        GPIO.output(MOTORPINS["pin1B"],GPIO.LOW)
        GPIO.output(MOTORPINS["pin1E"],GPIO.HIGH)
        
        time.sleep(10)
        
        print "Stopping motor"
        GPIO.output(MOTORPINS["pin1E"],GPIO.LOW)
    
    finally: 
        GPIO.output(MOTORPINS["pin1E"],GPIO.LOW)
        GPIO.cleanup()
    
    return render_template('motor.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
