import pandas as pd
from api import app
from flask import json, request, jsonify, g, make_response, abort, redirect
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory
from ..controllers.DataHandler import DataHandler
from ..controllers.ModelHandler import ModelHandler

#Global Imports
global datahandler
global modelhandler 

@app.route("/api/create/data", methods=["POST"])
def create_data():
   # https://drive.google.com/file/d/1dcDUnZcCOpQJdspssXoxueJZiXBDYeNK/view?usp=sharing
    if request.method == 'POST':
        global datahandler
        url='https://drive.google.com/uc?id=' + request.json["fileurl"].split('/')[-2]
        dataframe = pd.read_csv(r".././datasets/Heart Disease -  Binary Classification/Heart Disease - Training.csv")
        datahandler = DataHandler(dataframe)
        return jsonify({"msg": "Dataset was created successfully"}), 200
    return jsonify({"message": "Method not Allowed"}), 405
    

@app.route("/api/create/model", methods=["POST"])
def create_model():
    if request.method == 'POST':
        global modelhandler
        modelhandler = ModelHandler(**request.json)
        return jsonify({"msg": "Training Model was created successfully"}), 200
    return jsonify({"message": "Method not Allowed"}), 405

@app.route("/api/data", methods=["GET"])
def get_data():
    return jsonify({"message": "This is a starter Flask Project"}), 200


@app.route("/api/data/remove/feature", methods=["POST"])
def remove_feature():
    if request.method == 'POST':
        global datahandler
        datahandler.removeFeature(request.json["featureName"])
        dataframe = datahandler.getDataFrame()
        print(dataframe)
        return jsonify({"msg": dataframe.to_json(orient = 'table')}), 200
    return jsonify({"message": "Method not Allowed"}), 405
    

@app.route("/api/data/remove/invalid", methods=["POST"])
def remove_invalid():
    if request.method == 'POST':
        global datahandler
        datahandler.removeInvalidData()
        dataframe = datahandler.getDataFrame()
        print(dataframe)
        return jsonify({"msg": dataframe.to_json(orient = 'table')}), 200
    return jsonify({"message": "Method not Allowed"}), 405

@app.route("/api/data/translate", methods=["POST"])
def translate_data():
    if request.method == 'POST':
        global datahandler
        datahandler.translateData()
        dataframe = datahandler.getDataFrame()
        print(dataframe)
        return jsonify({"msg": dataframe.to_json(orient = 'table')}), 200
    return jsonify({"message": "Method not Allowed"}), 405

@app.route("/api/data/normalize", methods=["POST"])
def normalize_data():
    if request.method == 'POST':
        global datahandler
        datahandler.normalizeData()
        dataframe = datahandler.getDataFrame()
        print(dataframe)
        return jsonify({"msg": dataframe.to_json(orient = 'table')}), 200
    return jsonify({"message": "Method not Allowed"}), 405


@app.route("/api/model/fit", methods=["POST"])
def fit(dataframe):
    return jsonify({"message": "This is a starter Flask Project"}), 200


@app.route("/api/model/predict", methods=["POST"])
def predict(dataframe):
    return jsonify({"message": "This is a starter Flask Project"}), 200
