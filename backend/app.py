from flask import Flask, jsonify, make_response
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure MongoDB connection
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_data():
    try:
        data = mongo.db.users.find_one()
        if data:
            return make_response(jsonify({'name': data['name']}), 200)
        return make_response(jsonify({'error': 'No data found'}), 404)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
