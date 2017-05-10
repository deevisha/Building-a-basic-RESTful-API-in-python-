from flask import Flask, request ,jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import time

 
e = create_engine('sqlite:///chinook.db') #creates an engine which connects to sqlite database
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = e.connect() # connect to database
        query = conn.execute("select * from invoices") # This line performs query and returns json result
        return {'invoices': [i[2] for i in query.cursor.fetchall()]} # Fetches third column that is InvoiceDates

api.add_resource(Employees, '/invoices') # Route_1



if __name__ == '__main__':
     app.run(port='7005')
     