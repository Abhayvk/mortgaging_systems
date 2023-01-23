
from flask import Flask, render_template
import os
import pymongo
from urllib.parse import quote_plus
import pprint

app=Flask(__name__)

picFolder=os.path.join('static','images')

app.config['UPLOAD_FOLDER']=picFolder

@app.route('/')
def hi():
    a=os.path.join(app.config['UPLOAD_FOLDER'], 'user.jpg')
    return render_template('homepage.html',user_image=a)



@app.route('/contactus')
def index():
    return render_template('contact.html')

@app.route('/privacyterms')
def terms():
    return render_template('privacyterms.html')

@app.route('/about')
def hello():
    return render_template('about.html')

@app.route('/signin')
def hoo():
    return render_template('signup.html')

@app.route('/welcome')
def hihi():
    pic1=os.path.join(app.config['UPLOAD_FOLDER'], 'pawnbroker.jpg')
    return render_template('welcome.html',user_image=pic1)

if __name__=='__main__':
    app.run(debug=True)

import pymongo
from urllib.parse import quote_plus
import pprint

username = quote_plus('Abhayvk')
password = quote_plus('Abhay@123')

url = 'mongodb+srv://' + username + ':' + password + '@cluster0.wk5up6p.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(url, serverSelectionTimeoutMS=5000)
db = client['project1']
#To create and post a database in Mongodb
id_card = {
    'Name': "ch vinay",
    "Branch": "CSE-hons",
    "Gyear":"2025"
}

