# IMPORTS
from flask import Flask, jsonify, request  # Flask application which allows endpoints to be made
# this is importing the defined functions used to return data from the db, so they can be called here
from db_utils import get_animals_data, get_one_animals_data, add_new_animal
# This links the api (this file) to the clients file, so they will run together
app = Flask(__name__)
# ENDPOINTS
# 1. Introduction page in web browser
@app.route('/')
def index():
    return "Welcome to this animal data API!"
# 2. Returns all animal names
@app.route('/animals_data')
def get_all_animals():
    res = get_animals_data()
    return jsonify(res)
# 3. Returns all data for specified animal by name
@app.route('/animals_data/<view_animal>')
def get_one_animal(view_animal):
    res = get_one_animals_data(view_animal)
    return jsonify(res)
# 4. Puts the inserted data into the MYSQL database
@app.route('/animal', methods=['PUT'])
def add_animal():
    animal = request.get_json()
    add_new_animal(
        id=animal['id'],
        animal_name=animal['animal_name'],
        baby_name=animal['baby_name'],
        lifespan_avg_years=animal['lifespan_avg_years'],
        habitat=animal['habitat'],
        adult_diet=animal['adult_diet'],
    )
    return "You Have Added a New Animal"
# Connects api to user app, so they can run together
if __name__ == '__main__':
    app.run(debug=True)
