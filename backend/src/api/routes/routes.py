from api import app
from flask import json, request, jsonify, g, make_response, abort, redirect
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory
from ..controllers.DataHandler import DataHandler
from ..controllers.ModelHandler import ModelHandler

#Global Imports
global datahandler
global modelhandler 

# @app.route("/api/create/data", method=["POST"])
# def create_datahandler(fileurl):
#     url='https://drive.google.com/uc?id=' + fileurl.split('/')[-2]
#     data = pd.read_csv(url)
#     dataframe = pd.DataFrame(data)
#     datahandler = DataHandler(dataframe)
#     print(datahandler)
#     return jsonify({"message": "This is a starter Flask Project"}), 201

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
