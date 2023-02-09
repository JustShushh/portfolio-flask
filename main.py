import csv
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb+srv://angie:5OoZySALBusNjnef@portfolioadb.dn8gkkn.mongodb.net/?retryWrites=true&w=majority")
mycol = client.database
#mycol = client["database"]

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        write_to_email(data)
        write_to_message(data)
        write_to_subject(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong!'

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(csvfile)
        writer.writerow([email, subject, message])
    return True

def write_to_email(data):
        email = data['email']
        df=pd.read_csv("database.csv")
        client.database.email.insert_one( {email : 'email'} )

def write_to_subject(data):
        subject = data['subject']
        df=pd.read_csv("database.csv")
        client.database.subject.insert_one( {subject : 'subject'} )
  

def write_to_message(data):
        message = data['message']
        df=pd.read_csv("database.csv")
        client.database.message.insert_one( {message : 'message'} )
        