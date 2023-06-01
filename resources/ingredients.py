import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import login_required, current_user
ingredients = Blueprint('ingredients', 'ingredient')


#INDEX Route
@ingredients.route('/ingredients', methods =["GET"])
@login_required
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
@ingredients.route('/ingredients/<id>', methods = ["DELETE"])
@login_required
def delete_ingredient(id):
    delete_query = models.Ingredient.delete().where(models.Ingredient.id == id)
    num_rows_deleted = delete_query.execute()
    print(num_rows_deleted)
    return jsonify(
        data={},
        message=f"Successfully deleted {num_rows_deleted} dog with id of {id}.",
        status = 200
    ), 200

#UPDATE Route
@ingredients.route('/ingredients/<id>', methods=["PUT"])
@login_required
def update_ingredient(id):
    payload= request.get_json()
    print(payload)
    models.Ingredient.update(**payload).where(models.Ingredient.id == id).execute()
    return jsonify(
        data = model_to_dict(models.Ingredient.get_by_id(id)),
        message = "Updated ingredient successfully!",
        status = 200
    ), 200

#CREATE Route
@ingredients.route('/ingredients', methods=["POST"])
@login_required
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
@ingredients.route('/ingredients/<id>', methods=["GET"])
@login_required
def get_one_ingredient(id):
    ingredient = models.Ingredient.get_by_id(id)
    print(ingredient)
    return jsonify(
        data=model_to_dict(ingredient),
        message="Successfully showing one ingredient by id!",
        status=200
    ), 200