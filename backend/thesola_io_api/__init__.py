from flask import Flask, request, make_response, jsonify

from .nowplaying import get_nowplaying

__version__ = "0.dev1"

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify(who="thesola.io-api"), 200

@app.route('/nowplaying', methods=['GET'])
def nowplaying():
    return jsonify(get_nowplaying())
