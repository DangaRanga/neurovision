from pyexpat import model
import pandas as pd
from api import app
from flask import json, request, jsonify, g, make_response, abort, redirect
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory
from ..controllers.DataHandler import DataHandler
from ..controllers.ModelHandler import ModelHandler
from ..util import dataset_util
from ..controllers.prep import prepHRT
from ..globals import *


@app.route("/api/create/data", methods=["POST"])
def create_data():
    global datahandler
   # https://drive.google.com/file/d/1dcDUnZcCOpQJdspssXoxueJZiXBDYeNK/view?usp=sharing
    if request.method == 'POST':
        # url='https://drive.google.com/uc?id=' + request.json["fileurl"].split('/')[-2]
        dataframe = pd.read_csv(
            r"../datasets/Heart Disease -  Binary Classification/Heart Disease - Training.csv")
        datahandler = DataHandler(dataframe)
        return jsonify({"msg": "Dataset was created successfully"}), 200
    return jsonify({"msg": "Method not Allowed"}), 405


@app.route("/api/create/model", methods=["POST"])
def create_model():
    global modelhandler
    if request.method == 'POST':
        modelhandler = ModelHandler(**request.json)
        modelhandler.createModel()
        return jsonify({"msg": "Training Model was created successfully"}), 200
    return jsonify({"msg": "Method not Allowed"}), 405


@app.route("/api/data", methods=["GET"])
def get_data():
    dataset_names = ['heart_disease', 'house_price', 'iris']

    if request.method == "GET":
        # Retrieve and initialize dataset based on request
        selection = request.args.get('dataset')
        if selection not in dataset_names:
            return jsonify({"error": f"Invalid Dataset Entered: {selection}"}), 400

        # Create dataframe for dataset
        dataset = dataset_util.initialize_dataset(selection)

        # Create data handler
        datahandler = DataHandler(dataset)

        # Convert the dataset to JSON to be sent
        result = datahandler.toJSON()
        return jsonify({"msg": "Data Transmission Successful", "dataset": result}), 200

    return jsonify({"msg": "Method not Allowed"}), 405


@app.route("/api/data/remove/feature", methods=["POST"])
def remove_feature():
    global datahandler
    if request.method == 'POST':
        if type(datahandler) == DataHandler:
            datahandler.removeFeature(request.json["featureName"])
            result = datahandler.toJSON()
            return jsonify({"msg": "Feature has been removed succesfully", "dataset": result}), 200
        else:
            return jsonify({"msg": "Data Handler of Dataset has not been initialized"}), 500
    return jsonify({"msg": "Method not Allowed"}), 405


@app.route("/api/data/remove/invalid", methods=["POST"])
def remove_invalid():
    global datahandler
    if request.method == 'POST':
        if type(datahandler) == DataHandler:
            datahandler.removeInvalidData()
            result = datahandler.toJSON()
            return jsonify({"msg": "Invalid Data has been removed succesfully", "dataset": result}), 200
        else:
            return jsonify({"msg": "Data Handler of Dataset has not been initialized"}), 500
    return jsonify({"msg": "Method not Allowed"}), 405


@app.route("/api/data/translate", methods=["POST"])
def translate_data():
    global datahandler
    if request.method == 'POST':
        if type(datahandler) == DataHandler:
            datahandler.translateData()
            result = datahandler.toJSON()
            return jsonify({"msg": "Features have been tanslated succesfully", "dataset": result}), 200
        else:
            return jsonify({"msg": "Data Handler of Dataset has not been initialized"}), 500
    return jsonify({"msg": "Method not Allowed"}), 405


@app.route("/api/data/normalize", methods=["POST"])
def normalize_data():
    global datahandler
    if request.method == 'POST':
        if type(datahandler) == DataHandler:
            datahandler.normalizeData()
            result = datahandler.toJSON()
            return jsonify({"msg": "Dataset has been normalized", "dataset": result}), 200
        else:
            return jsonify({"msg": "Data Handler of Dataset has not been initialized"}), 500
    return jsonify({"msg": "Method not Allowed"}), 405


@app.route("/api/model/fit", methods=["POST"])
def fit():
    global datahandler, modelhandler
    if request.method == 'POST':
        if type(datahandler) == DataHandler and type(modelhandler) == ModelHandler:
            datahandler.dataset_split(request.json["train"])
            training_features = datahandler.x_train
            training_output = datahandler.y_train
            result = modelhandler.train(training_features, training_output)
            return jsonify({"msg": "Model has been trained. You can view the results of the training here", "dataset": result}), 200
        else:
            return jsonify({"msg": "Data Handler of Dataset and the Training Model have not been initialized"}), 500
    return jsonify({"msg": "Method not Allowed"}), 405


@app.route("/api/model/evaluate", methods=["GET"])
def evaluate():
    global datahandler, modelhandler
    if request.method == 'GET':
        if type(datahandler) == DataHandler and type(modelhandler) == ModelHandler:
            test_features = datahandler.x_test
            test_output = datahandler.y_test
            result = modelhandler.evaluate(test_features, test_output)
            return jsonify({"msg": "Evaluation conducted.", "dataset": result}), 200
        else:
            return jsonify({"msg": "Data Handler of Dataset and the Training Model have not been initialized"}), 500
    return jsonify({"msg": "Method not Allowed"}), 405


@app.route("/api/model/predict", methods=["POST"])
def predict():
    global modelhandler
    if request.method == 'POST':
        if type(modelhandler) == ModelHandler:
            if request.json["problem"] == "HRT":
                dataframe = pd.read_csv(
                    r"./datasets/Heart Disease -  Binary Classification/Exploration - Heart Disease.csv")
                hndlr = DataHandler(dataframe)
                hndlr = prepHRT(hndlr)
                features = hndlr.x_test
            result = modelhandler.predict(features)
            return jsonify({"msg": "Prediction was Successful", "dataset": result}), 200
        else:
            return jsonify({"msg": "The Training Model have not been initialized"}), 500
    return jsonify({"msg": "Method not Allowed"}), 405
