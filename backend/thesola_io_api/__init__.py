from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin

from .nowplaying import get_nowplaying

__version__ = "0.dev1"

app = Flask(__name__)
cors = CORS(app,
            origins = ["http://127.0.0.1:8080", "https://thesola.io"],
            methods = ['GET'])
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def hello():
    return jsonify(who="thesola.io-api"), 200

@app.route('/nowplaying', methods=['GET'])
@cross_origin()
def nowplaying():
    return jsonify(get_nowplaying())
