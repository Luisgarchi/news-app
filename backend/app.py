from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure MongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/news"
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_data():
    data = mongo.db.users.find_one()
    return jsonify({'name': data['name']})

if __name__ == '__main__':
    app.run(debug=True)