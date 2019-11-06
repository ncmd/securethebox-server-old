from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# API Paths

if __name__ == '__main__':
    app.run(debug=True)
