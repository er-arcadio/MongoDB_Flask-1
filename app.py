# ---- YOUR APP STARTS HERE ----

# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from pymongo import MongoClient  # to interact with MongoDB
import os    # to use a secret environmental variable


# -- Initialization section --
app = Flask(__name__)


events = [
  {"event":"First Day of Classes", "date":"2019-08-21"},
  {"event":"Winter Break", "date":"2019-12-20"},
  {"event":"Finals Begin", "date":"2019-12-01"},
  {"event":"Spring Break", "date":"2019-4-15"}
]

# Set your password as a secret env variable
password = os.environ['mongo_password']

# Set up URI of database as a "client"
client = MongoClient(f'mongodb+srv://admin:{password}@cluster0.0argbbr.mongodb.net/?retryWrites=true&w=majority')

# This should be client.<nameOfDatabase>
db = client.database


# -- Routes section --

# INDEX
@app.route('/')
@app.route('/index')
def index():

  collection = db.events
  events = collection.find({})
  return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA
@app.route('/add')
def add():
  # connect to the specific sub database
  collection = db.events
  # insert new data
  collection.insert_one({"event":"Birthday", "date":"2022-01-18"})
  # return a message to the user
  return "Event added"
