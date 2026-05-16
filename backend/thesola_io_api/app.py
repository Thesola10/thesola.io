from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin

from . import app
from .nowplaying import get_nowplaying, get_one_song
from .badge import dispense_badge

@app.route('/', methods=['GET'])
@cross_origin()
def hello():
    return jsonify(who="thesola.io-api"), 200

@app.route('/nowplaying', methods=['GET'])
@cross_origin()
def nowplaying():
    return jsonify(get_nowplaying())

@app.route('/timeout', methods=['GET'])
@cross_origin()
def timeout():
    return jsonify(get_one_song())

@app.route('/nowplaying.badge', methods=['GET'])
@cross_origin()
def get_badge():
    track = request.args.get('eval')
    token = request.args.get('turnstile')
    return dispense_badge(track, token)
