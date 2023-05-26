from flask import Flask, jsonify, request
import models
import requests
from resources.ingredients import ingredients
from resources.users import users
from flask_login import LoginManager, login_required
from flask_cors import CORS

DEBUG = True
PORT = 8000

app = Flask(__name__)
CORS(app)
CORS(ingredients, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(ingredients, url_prefix='/api')
app.register_blueprint(users, url_prefix='/api')
app.secret_key = "loukeysmashlou"

login_manager = LoginManager()
login_manager.init_app(app)

def load_user(user_id):
    return models.User.get(models.User.id == user_id)

@app.route('/ingredients/api/search', methods=['POST'])
def search_by_ingredients():
    # Get the ingredients from the request
    ingredients = request.json['ingredients']

    # Make a request to the MealDB API
    response = requests.get(f'https://www.themealdb.com/api/json/v2/9973533/filter.php?i={",".join(ingredients)}')

    # Return the response from the MealDB API
    return jsonify(response.json())

@app.route('/')
def home():
    return 'hi'

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)