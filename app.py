from io import StringIO
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify,render_template, url_for
import os 
import pickle

#create the flask app
app = Flask(__name__)

#Image Handling in index.html User Intarface page
imageFolder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = imageFolder

#Load the pickle model
training_model = pickle.load(open("training_model.pkl", "rb"))

#define the Html page from where you get the html user inputs.Simply the Home UI page.
@app.route("/")
def index():
    demo_image = os.path.join(app.config['UPLOAD_FOLDER'],'market.jpg')
    return render_template('index.html',user_image = demo_image)


if __name__ == "__main__":
    app.run(debug=True) 