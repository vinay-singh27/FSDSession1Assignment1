import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle,os
import sys

sys.path.append('../1.Development/')

from config import modeloutput

# Create flask app
flask_app = Flask(__name__,template_folder='templates')
model = pickle.load(open(modeloutput, "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [x for x in request.form.values()]
    float_features = list(filter(None, float_features))
    rawinput = [np.array(float_features)]
    input_feats = [x for x in request.form.keys()]
    input_data = dict(zip(input_feats,float_features))
    
    #Exception Handling from utility.py
    #Feature Enginnering from feature.py

    return render_template("index.html", prediction_text = "Incorrect {}".format([k for k, v in check_list.items() if not v]))
if __name__ == "__main__":
    flask_app.run(debug=True)