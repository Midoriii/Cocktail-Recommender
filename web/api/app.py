from flask import Flask, request, jsonify
from recommend import Recommend

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def index():
    data = request.json
    recommended_drinks = Recommend(data['indices'], data['count'])
    return jsonify(recommended_drinks)

# @app.route('/ratings', methods=['POST'])
# def index():
#     data = request.json
#     return jsonify(len(data['indices']))

# @app.route('/rate', methods=['POST'])
# def index():
#     data = request.json
#     return jsonify(len(data['indices']))