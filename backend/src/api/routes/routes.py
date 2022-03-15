from api import app
from flask import json, request, jsonify, g, make_response, abort, render_template


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "This is a starter Flask Project"}), 200

@app.route("/getdata", methods=["GET"])
def getdata(name):
    pass

@app.route("/remove_field", methods=["POST"])
def remove_field(fieldname, dataframe):
    pass

@app.route("/normalize", methods=["POST"])
def normalize(dataframe):
    pass