from flask import (render_template, Blueprint)
import RPi.GPIO as GPIO
import time

bp = Blueprint('motor', __name__, url_prefix='/motor')

MOTORPINS = {"pin1A": 36, "pin1B": 38, "pin1E":40}
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTORPINS["pin1A"], GPIO.OUT)
GPIO.setup(MOTORPINS["pin1B"], GPIO.OUT)
GPIO.setup(MOTORPINS["pin1E"], GPIO.OUT)


@bp.route('/run',methods=["GET"])
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
