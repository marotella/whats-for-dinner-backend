from flask import Flask, jsonify, request
import models
import requests
from resources.ingredients import ingredients
from resources.users import users
from flask_login import LoginManager, login_required
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
PORT = os.environ.get("PORT")
print(os.environ.get("PORT"))

app = Flask(__name__)
CORS(app)
CORS(ingredients, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
app.secret_key = os.environ.get("APP_SECRET")
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except:
        return None

app.register_blueprint(ingredients, url_prefix='/api')
app.register_blueprint(users, url_prefix='/api')

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    return response

@app.route('/ingredients/api/search', methods=['POST'])
@login_required
def search_by_ingredients():
    ingredients = request.json['ingredients']
    response = requests.get(f'https://www.themealdb.com/api/json/v2/9973533/filter.php?i={",".join(ingredients)}')
    return jsonify(response.json())

@app.route("/ingredients/api/recipes/<recipe_id>", methods=["GET"] )
def get_recipe_data(recipe_id):
    response = requests.get(f'https://www.themealdb.com/api/json/v1/1/lookup.php?i={recipe_id}')
    if response.status_code == 200:
        data = response.json()
        if data['meals'] is not None:
            recipe = data['meals'][0]
            recipe_data = {
                'id': recipe['idMeal'],
                'name': recipe['strMeal'],
                'thumbnail': recipe['strMealThumb'],
                'category': recipe['strCategory'],
                'area': recipe['strArea'],
                'instructions': recipe['strInstructions'],
                'ingredients': [],
            }
            for i in range(1, 21):
                ingredient_key = f'strIngredient{i}'
                measure_key = f'strMeasure{i}'
                ingredient = recipe.get(ingredient_key)
                measure = recipe.get(measure_key)
                if ingredient and measure:
                    recipe_data['ingredients'].append({
                        'ingredient': ingredient,
                        'measure': measure
                    }) 
            return jsonify(recipe_data)
        else:
            return jsonify({'error': 'Recipe not found'})
    else:
        return jsonify({'error': 'Failed to retrieve recipe'})                        

@app.route('/')
def home():
    return 'hi'
# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)