from flask import render_template
from flask import request
from flask_api import FlaskAPI
import motor
import glonassgps
app = FlaskAPI(__name__)

app.register_blueprint(motor.bp)
app.register_blueprint(glonassgps.bp)

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
