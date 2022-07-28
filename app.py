from flask import Flask
from maintanance.logger import logging
from maintanance.exception import maintananceException
import sys
import os
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception('we are testing custom exception')
    except Exception as e:
        maintanance=maintananceException(e,sys)
        logging.info(maintanance.error_message)
        logging.info("we are testing logging module")
    return "CI CD pipeline has been established."

if __name__=="__main__":
    app.run(debug=True)