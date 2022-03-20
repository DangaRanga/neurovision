from src.api import app
from flask import json, request, jsonify, g, make_response, abort, redirect


# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def home():
#     return redirect("/api", 200)
    # return jsonify({"message": "This is a starter Flask Project"}), 200

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
