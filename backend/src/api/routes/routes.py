from api import app
from flask import json, request, jsonify, g, make_response, abort, render_template


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "This is a starter Flask Project"}), 200