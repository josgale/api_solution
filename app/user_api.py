from flask import Flask, request, jsonify
from database_connector import get_all_users, get_user_by_id, post_user

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = get_all_users()
        response = {
            'users': users
        }
        return jsonify(response), 200
    except Exception as e:
        response = {
            'error': str(e)
        }
        return jsonify(response), 500


@app.route('/users', methods=['POST'])
def create_user():
    try:
        user_data = request.get_json()
        user_id = user_data['id']
        name = user_data['user_name']
        post_user(user_id, name)
        response = {
            'message': 'User created successfully'
        }
        return jsonify(response), 200
    except Exception as e:
        response = {
            'error': str(e)
        }
        return jsonify(response), 500


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = get_user_by_id(user_id)
        if user:
            response = {
                'user_name': user
            }
            return jsonify(response), 200
        else:
            response = {
                'message': 'User not found'
            }
            return jsonify(response), 404
    except Exception as e:
        response = {
            'error': str(e)
        }
        return jsonify(response), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
