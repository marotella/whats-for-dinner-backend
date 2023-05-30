import models 
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, logout_user, current_user, login_required
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
            data={},
            message = "A user with that email already exists",
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
        created_user_dict=model_to_dict(created_user)
        print(created_user_dict)
        print(type(created_user_dict['password']))
        created_user_dict.pop('password')
        return jsonify(
            data=created_user_dict,
            message=f"Successfully registered user {created_user_dict['email']}",
            status=201
        ), 201


#SIGNIN ROUTE
@users.route("/users/login", methods=['POST'])
def login():
    payload= request.get_json()
    payload['email']=payload['email'].lower()
    payload['username']=payload['username'].lower()
    try:
        user=models.User.get(models.User.email == payload['email'])
        user_dict= model_to_dict(user)
        password_is_correct= check_password_hash(user_dict['password'], payload['password'])
        if (password_is_correct):
            login_user(user)
            print(f"{current_user.username} is current_user.username in POST login")
            return jsonify(
                data=user_dict,
                message=f"Successfully logged in {user_dict['email']}",
                status=200
            ), 200
        else:
            # the password is bad
            print("login is no good")
            return jsonify(
                data={},
                message="Email or password is incorrect", # let's be vague
                status=401
            ), 401

    except models.User.DoesNotExist:
        # else if they don't exist
        print('account does not exist')
        # respond -- bad username or password
        return jsonify(
            data={},
            message="Email or password is incorrect", # let's be vague
            status=401
        ), 401
        
@users.route('/users/logged_in_user', methods=['GET'])
def get_logged_in_user():
    # https://flask-login.readthedocs.io/en/latest/#flask_login.current_user
    # we can access the current_user because we called login_user and setup user_loader
    print(current_user)
    print(type(current_user)) # <class 'werkzeug.local.LocalProxy'> # google it if you're interested
    print(f"{current_user.username} is current_user.username in GET logged_in_user")
    user_dict = model_to_dict(current_user)
    user_dict.pop('password')

    # OBSERVER -- YOU now have access to the currently logged in user
    # anywhere you want user current_user
    return jsonify(data=user_dict), 200

# we need a logout route

#LOGOUT ROUTE
@users.route("/users/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify(
        data={},
        message="Successfully logged out",
        status=200
    ), 200
    

    