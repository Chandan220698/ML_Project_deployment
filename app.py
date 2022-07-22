from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    try:
        raise Exception("We are testing the exception")
    except Exception as e:
        housing_object = HousingException(e, sys)
        logging.info(housing_object.error_message)
        logging.info("We are testing logging module")
        
    return "Hello World !"

if __name__ == "__main__":
    app.run(debug = True)