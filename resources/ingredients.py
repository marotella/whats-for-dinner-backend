import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import login_required, current_user
ingredients = Blueprint('ingredients', 'ingredient')


#INDEX Route
@ingredients.route('/ingredients', methods =["GET"])
def ingredients_index():
    result = models.Ingredient.select()
    print("Result of index request")
    print(result)
    ingredient_ditcs = [model_to_dict(ingredient)for ingredient in result]
    return jsonify({
        'data': ingredient_ditcs,
        'message': f"Successfully found {len(ingredient_ditcs)} ingredients!", 
        'status': 200
    }), 200
#DELETE Route


#UPDATE Route


#CREATE Route
@ingredients.route('/ingredients', methods=["POST"])
def create_ingredient():
    payload = request.get_json()
    print(payload)
    new_ingredient = models.Ingredient.create(ingredient=payload['ingredient'], quantity=payload['quantity'])
    print(new_ingredient)
    ingredient_dict = model_to_dict(new_ingredient)
    return jsonify(
        data=ingredient_dict,
        message="Successfully created and added ingredient!",
        status =201
    ), 201

#SHOW ROUTE