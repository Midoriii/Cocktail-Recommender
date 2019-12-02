from flask import Flask, request, jsonify
from recommend import Recommend, get_drink

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    recommended_drinks = Recommend(data['indices'], data['count'])
    return jsonify(recommended_drinks)

@app.route('/drink/<int:drink_id>', methods=['GET'])
def drink(drink_id):
    drink = get_drink(drink_id, None)
    return drink

# @app.route('/rate', methods=['POST'])
# def index():
#     data = request.json
#     return jsonify(len(data['indices']))