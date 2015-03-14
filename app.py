 #import the Flask class from the flask module
from flask import Flask, render_template, jsonify, request
from weatherscrape import *


# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/weather')
def weather():
    forecast_ob1=findweather('Varanasi', '12', '12')
    
    return request.query_string,jsonify(one=forecast_ob1[0], two=forecast_ob1[1], three=forecast_ob1[2]) # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
