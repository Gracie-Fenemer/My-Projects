# IMPORTS
import mysql.connector  # connects the MYSQL database and allows queries to be written in python
from config import USER, PASSWORD, HOST  # the private username and password stored in config.py
# Exception handling
class DbConnectionError(Exception):
    pass
# DEFINED FUNCTIONS
# First function initiates a connection to the MYSQL db specified in other functions
def get_db_connection(db_name):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return connection
# Function calls the connection to db and specifies the database
# This will return all animal names in the db in alphabetical order
def get_animals_data():
    try:
        db_name = 'animals_app'
        connection = get_db_connection(db_name)
        print('Connected to DB: %s' % db_name)
        cursor = connection.cursor(dictionary=True)
        query = """SELECT animal_name FROM animals_data ORDER BY animal_name;"""
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        print(result)
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if connection:
            connection.close()
            print("DB connection is closed")
    return result
# Function returns the whole row of data from db for the inputted animal
def get_one_animals_data(view_animal):
    try:
        db_name = 'animals_app'
        connection = get_db_connection(db_name)
        cursor = connection.cursor(dictionary=True)
        query = f"""SELECT * FROM animals_data WHERE animal_name = '{view_animal}';"""
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        print(result)
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if connection:
            connection.close()
            print("DB connection is closed")
    return result
# Function allows user to insert a new animal's data to the database
def add_new_animal(animal_name, id, baby_name, lifespan_avg_years, habitat, adult_diet):
    try:
        db_name = 'animals_app'
        connection = get_db_connection(db_name)
        cursor = connection.cursor(dictionary=True)
        values = f"'{id}','{animal_name}','{baby_name}','{lifespan_avg_years}','{habitat}','{adult_diet}'"
        query = f"""INSERT 
            INTO animals_data (id, animal_name, baby_name, lifespan_avg_years, habitat, adult_diet )
            VALUES ({values});"""
        cursor.execute(query)
        connection.commit()  # Saves the data to the db
        cursor.close()
        print("New animal added!")
    except Exception:
        raise DbConnectionError("Failed to read data from DB")
    finally:
        if connection:
            connection.close()
            print("DB connection is closed")
