from flask import Flask, request ,jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from datetime import datetime
from dateutil.parser import parse
import pandas as pd

#db_connect = create_engine('sqlite:///date.db') #creates an engine which connects to sqlite database
app = Flask(__name__)
api = Api(app)




class number(Resource):
    def get(self):
        dt = parse(raw_input("give input"))
        return(dt.strftime('%d-%m-%Y'))


api.add_resource(number, '/dates') # Route_1


if __name__ == '__main__':
     app.run(port='5002')
     



