import os
import pandas as pd
from api import app
from security.jwt import decodetoken, checktoken
from flask import json, request, jsonify, g, make_response, abort, redirect
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory
from controllers.DataHandler import DataHandler



# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def home():
#     return redirect("/api", 200)
# return jsonify({"message": "This is a starter Flask Project"}), 200
global datahandler

@app.route("/api/create/datahandler", method=["POST"])
def create_datahandler(fileurl):
    url='https://drive.google.com/uc?id=' + fileurl.split('/')[-2]
    data = pd.read_csv(url)
    dataframe = pd.DataFrame(data)
    datahandler = DataHandler(dataframe)
    print(datahandler)
    return jsonify({"message": "This is a starter Flask Project"}), 201

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "This is a starter Flask Project"}), 200


@app.route("/api/data/remove", methods=["POST"])
def remove_feature(feature, dataframe):
    return jsonify({"message": "This is a starter Flask Project"}), 200


@app.route("/api/data/normalize", methods=["POST"])
def normalize():
    return jsonify({"message": "This is a starter Flask Project"}), 200


@app.route("/api/model/fit", methods=["POST"])
def fit(dataframe):
    return jsonify({"message": "This is a starter Flask Project"}), 200


@app.route("/api/model/predict", methods=["POST"])
def predict(dataframe):
    return jsonify({"message": "This is a starter Flask Project"}), 200
