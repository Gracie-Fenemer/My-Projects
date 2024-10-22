DROP DATABASE IF EXISTS animals_app;
CREATE DATABASE animals_app;

USE animals_app;

CREATE TABLE animals_data (
id INT,
animal_name VARCHAR(15) NOT NULL,
baby_name VARCHAR(15),
lifespan_avg_years INT,
habitat VARCHAR(20),
adult_diet VARCHAR(15)
);

INSERT INTO animals_data 
(id, animal_name, baby_name, lifespan_avg_years, habitat, adult_diet)
VALUES
(1, 'Sea Turtle', 'Hatchling', 70, 'Marine', 'Herbivore'),
(2, 'Wombat', 'Joey', 15, 'Forest/Woodland', 'Herbivore');
