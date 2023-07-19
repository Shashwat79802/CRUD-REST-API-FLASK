from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)

connection_string = os.environ["CONNECTION_STRING"]
database = os.environ["DATABASE"]
db_collection = os.environ["COLLECTION"]

client = MongoClient(connection_string)
db = client[database]
collection = db[db_collection]


# GET /users - Returns a list of all users
@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find())
    return dumps(users)


# GET /users/<id> - Returns the user with the specified ID
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = collection.find_one({'_id': ObjectId(id)})
    if user:
        return dumps(user)
    else:
        return jsonify({'error': 'User not found'}), 404


# POST /users - Creates a new user with the specified data
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if 'name' in data and 'email' in data and 'password' in data:
        user = {
            'name': data['name'],
            'email': data['email'],
            'password': data['password']
        }
        result = collection.insert_one(user)
        return jsonify({'message': 'User created', 'id': str(result.inserted_id)}), 201
    else:
        return jsonify({'error': 'Missing required fields'}), 400


# PUT /users/<id> - Updates the user with the specified ID with the new data
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    if 'name' in data or 'email' in data or 'password' in data:
        update_fields = {}
        if 'name' in data:
            update_fields['name'] = data['name']
        if 'email' in data:
            update_fields['email'] = data['email']
        if 'password' in data:
            update_fields['password'] = data['password']
        result = collection.update_one({'_id': ObjectId(id)}, {'$set': update_fields})
        if result.modified_count > 0:
            return jsonify({'message': 'User updated'})
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Missing fields to update'}), 400


# DELETE /users/<id> - Deletes the user with the specified ID
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'User deleted'})
    else:
        return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


# from flask import Flask, json, jsonify
# from flask_restful import Api, Resource, reqparse
# from pymongo import MongoClient
# from bson.objectid import ObjectId
# from bson.json_util import dumps
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)
# api = Api(app)

# connection_string = os.environ["CONNECTION_STRING"]
# database = os.environ["DATABASE"]
# db_collection = os.environ["COLLECTION"]

# # MongoDB connection
# client = MongoClient(connection_string)
# db = client[database]
# collection = db[db_collection]


# class UserResource(Resource):

#     def get(self, user_id=None):
#         if user_id:
#             user = collection.find_one({'_id': ObjectId(user_id)})
#             if user:
#                 user["_id"] = str(user["_id"])
#                 return jsonify(user)
#             else:
#                 return {'error': 'User not found'}, 404
#         else:
#             users = list(collection.find())
#             for data_dict in users:
#                 data_dict["_id"] = str(data_dict["_id"])

#             return jsonify(users)

#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str, required=True)
#         parser.add_argument('email', type=str, required=True)
#         parser.add_argument('password', type=str, required=True)
#         args = parser.parse_args()

#         user = {
#             'name': args['name'],
#             'email': args['email'],
#             'password': args['password']
#         }
#         result = collection.insert_one(user)
#         return {'message': 'User created', 'id': str(result.inserted_id)}, 201

#     def put(self, user_id):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str)
#         parser.add_argument('email', type=str)
#         parser.add_argument('password', type=str)
#         args = parser.parse_args()

#         update_fields = {}
#         for field in ['name', 'email', 'password']:
#             if args[field]:
#                 update_fields[field] = args[field]

#         result = collection.update_one({'_id': ObjectId(user_id)}, {'$set': update_fields})
#         if result.modified_count > 0:
#             return {'message': 'User updated'}
#         else:
#             return {'error': 'User not found'}, 404

#     def delete(self, user_id):
#         result = collection.delete_one({'_id': ObjectId(user_id)})
#         if result.deleted_count > 0:
#             return {'message': 'User deleted'}
#         else:
#             return {'error': 'User not found'}, 404


# # API routes
# api.add_resource(UserResource, '/users', '/users/<string:user_id>')

# if __name__ == '__main__':
#     app.run(debug=True)
