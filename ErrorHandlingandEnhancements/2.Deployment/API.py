import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle,os
import sys
from schema import SchemaError

sys.path.append('../1.Development/')

from config import modeloutput
from common_util.utility import exceptions, parse_error_message
from common_util.features import process

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
    input_feats = [x for x in request.form.keys()]
    input_data = dict(zip(input_feats,float_features))
    
    #Exception Handling from utility.py
    output, error_status = exceptions(input_data)
    if not error_status :
        prepared_input_data = process(output)
        input_array = np.array(list(output.values())).reshape(1,-1)
        prediction = model.predict(input_array)
        final_msg = "Predicted Value: " + prediction
    else :
        final_msg = "Error: " + output


    return render_template("index.html", prediction_text = final_msg)

    # return render_template("index.html", prediction_text = "Incorrect {}".format([k for k, v in check_list.items() if not v]))
if __name__ == "__main__":
    flask_app.run(debug=True)