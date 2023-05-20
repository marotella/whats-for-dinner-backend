from flask import Flask, jsonify, request
import models
import requests
DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.route('/ingredients/api/search', methods=['POST'])
def search_by_ingredients():
    # Get the ingredients from the request
    ingredients = request.json['ingredients']

    # Make a request to the MealDB API
    response = requests.get(f'https://www.themealdb.com/api/json/v2/9973533/filter.php?i={",".join(ingredients)}')

    # Return the response from the MealDB API
    return jsonify(response.json())

@app.route('/')
def index():
    return 'hi'

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)