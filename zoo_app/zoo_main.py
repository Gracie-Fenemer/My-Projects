# IMPORTS
import json
import requests
# DEFINED FUNCTIONS to get specified data from endpoints in app.py file
# This functions gets all data from the database
def get_animals():
    result = requests.get(f'http://localhost:5000/animals_data')
    # return the data receive from the api
    return result.json()
# This functions gets only data specified by one parameter such as animal_name
def get_all_animals_by_name(view_animal):
    result = requests.get(f'http://localhost:5000/animals_data/{view_animal}')
    # return the data receive from the api
    return result.json()
# This functions presents the returned data (animal_name) in a table format for clearer viewing
def display_data(records):
    # Print the names of the columns.
    print("{:<15} ".format(
        'ANIMALS'))
    print('-' * 25)
    # print each data item.
    for item in records:
        print("{:<15} ".format(
            item['animal_name']
        ))
# This functions presents the returned data (one specific animal and all the data)
# in a table format for clearer viewing
def display_one_animals_data(records):
    # Print the names of the columns.
    print("{:<15}, {:<15}, {:<15}, {:<15}, {:<15}, {:<15} ".format(
        'ANIMALS', 'ENCLOSURE NO.', 'DIET', 'BABY NAME', 'HABITAT', 'LIFESPAN (years)'))
    print('-' * 150)
    # print each data item.
    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
            item['animal_name'], item['id'], item['adult_diet'],
            item['baby_name'], item['habitat'], item['lifespan_avg_years']
        ))
# This functions stores the information needed for a PUT method in order to
# insert a new animal into the database
def add_new_animal(enclosure, name, baby_name, lifespan, habitat, diet):
    animal = {
        "id": enclosure,
        "animal_name": name,
        "baby_name": baby_name,
        "lifespan_avg_years": lifespan,
        "habitat": habitat,
        "adult_diet": diet,
    }
    response = requests.put(
        'http://localhost:5000/animal',
        headers={'content-type': 'application/json'},
        data=json.dumps(animal)
    )
# This function is the main app for the user. It collects user inputs which
# are used to return data from app.py and db_utils
def run():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Welcome to the zoo app!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    # If the user types 'y' then all animal names in the database are returned only
    view_all_animals = input('Would you like to view all the animals? (y/n): ')
    if view_all_animals == 'y':
        all_data = get_animals()
        display_data(all_data)
    else:
        print()
    print()
    # This allows the user to insert a new animal into the database
    new_animal = input('If the animal you want to see is not in this list would you like to add it?(y/n): ')
    add = new_animal == 'y'
    # These are the parameters that need information but only one is not null in MYSQL
    if add:
        print('Only questions with * are mandatory')
        enclosure = (int(input('*What is the number of the enclosure? Type the number: ')))
        name = input('*Enter animal\'s name (first letter needs a capital letter): ')
        baby_name = input('What are their babies called: ')
        lifespan = (int(input('*How many years do they live for: ')))
        habitat = input('Where do they live? marine/forest/desert/mountains/grassland: ')
        diet = input(f'What does the {name} eat? carnivore/herbivore/omnivore/other: ')
        add_new_animal(enclosure, name, baby_name, lifespan, habitat, diet)
        print(f'Thank you for adding a new animal!')
    else:
        print()
    # This returns one specific animal (could be the one they just inserted or different)
    view_animal = input('What animal would you like to look at (from the list): ')
    if view_animal:
        print(f'You have selected {view_animal}, we are fetching the info')
        print('Thanks for waiting, here is your info...')
        animal_info = get_all_animals_by_name(view_animal)
        display_one_animals_data(animal_info)
    else:
        print('Thank you for visiting!')
# This Allows You to Execute Code When the File Runs as a Script, not module.
if __name__ == '__main__':
    run()
