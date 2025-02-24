# Role : user RoleBasedAccessControl


from flask import Blueprint, request, jsonify
from functools import wraps
from flask_cors import cross_origin
import jwt
from datetime import datetime, timedelta
from config import Config


user = Blueprint("user", __name__)
USER_SECRET_KEY = Config.USER_SECRET_KEY


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 403
        try:
            token = token.split(" ")[1]  # Get token from "Bearer <token>"
            data = jwt.decode(token, USER_SECRET_KEY, algorithms=['HS256'])
            request.user = data
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired!"}), 403
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 403
        return f(*args, **kwargs)
    return decorated_function


def user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.user.get('role') != 'user':
            return jsonify({"message": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decorated_function


@user.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username is None or password is None:
        return jsonify({"message": "Missing username or password"}), 400
    
    if username == "" or password == "":
        return jsonify({"message": "Invalid username or password"}), 400

    if username == "user" and password == "user":
        token = jwt.encode({
            'user_id': 1,
            'username': "user",
            'role': "user",
            'exp': datetime.utcnow() + timedelta(hours=1)
        }, USER_SECRET_KEY, algorithm='HS256')
        return jsonify({"token": token, "role": "user"}), 200

    return jsonify({"message": "Invalid credentials"}), 401