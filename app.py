from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps


app = Flask(__name__)
client = MongoClient('mongodb+srv://shashwat79802:shashwat79802@cluster0.ota7y4c.mongodb.net/test')
db = client['Unheard']
collection = db['User']


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
