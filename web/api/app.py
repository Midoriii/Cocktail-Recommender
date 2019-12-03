from flask import Flask, request, jsonify
from recommend import Recommend, get_drink
from flask_cors import CORS
import simplejson

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    recommended_drinks = Recommend(data['indices'], data['count'])
    return simplejson.dumps(recommended_drinks, ignore_nan=True)


@app.route('/drink/<int:drink_id>', methods=['GET'])
def drink(drink_id):
    drink = get_drink(drink_id, None)
    return simplejson.dumps(drink, ignore_nan=True)

# @app.route('/rate', methods=['POST'])
# def index():
#     data = request.json
#     return jsonify(len(data['indices']))