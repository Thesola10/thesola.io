from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin

from . import app
from .nowplaying import get_nowplaying

@app.route('/', methods=['GET'])
@cross_origin()
def hello():
    return jsonify(who="thesola.io-api"), 200

@app.route('/nowplaying', methods=['GET'])
@cross_origin()
def nowplaying():
    return jsonify(get_nowplaying())
