import models 
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user

users = Blueprint('users', 'users')


#REGISTER ROUTE
@users.route("/users/register", methods=["POST"])
def register_user():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()
    print(payload)
    try:
        models.User.get(models.User.email == payload['email'])
        return jsonify(
            data={}
            message = "A user with that email already exists"
            status=401
        ), 401
    except models.DoesNotExist:
        pw_hash = generate_password_hash(payload['password'])
        created_user = models.User.create(
            username=payload['username'],
            email=payload['email'],
            password=pw_hash
        )
        login_user(created_user)
        created_user_dict=model_to_dict
        (created_user)
        print(created_user_dict)
        print(type(created_user_dict['password']))
        created_user_dict.pop('password')
        return jsonify(
            data=created_user_dict,
            message=f"Successfully registered user {created_user_dict['email']}",
            status=201
        ), 201


#SIGNIN ROUTE




#LOGOUT ROUTE