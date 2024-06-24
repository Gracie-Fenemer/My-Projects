/* This is a Customer Relationship Management (CRM) database specifically for a Hypnotherapy Practice to record and
 manage their customers, appointments and treatments.

It allows the Practitioner to store important information about the customer such as their: full name, title, gender, age, 
email, home number, address in the Customer table, appointments they have requested in the Appointment table and  
records which treatments they will given during the appointment.

The practice is able to analyse this data which assists the practitioner by showing the treatments used for clients,
to better understand effective treatments for different ages of women living in different locations.   
There is data to show the most common treatment.  

There is an example of a customer that cancelled their appointment. 
For this example I have deleted the data record from the Appointments table.  
The customer remains in the Customer table as they make another appointment in the future.*/


-- Create Database 
DROP database IF EXISTS hypnotherapy_crm;
CREATE DATABASE hypnotherapy_crm;
USE hypnotherapy_crm;

-- create customer table
CREATE TABLE Customers (
cust_ID INTEGER NOT NULL PRIMARY KEY, 
cust_Title CHAR(5) NULL,
cust_FirstName CHAR(50) NOT NULL,
cust_Surname CHAR(50) NOT NULL, -- not null constraint
cust_Gender CHAR(10) CHECK (cust_Gender='female') NOT NULL, -- chec
cust_Age INTEGER NOT NULL,
cust_Email CHAR(50),
cust_PhoneNumber BIGINT NOT NULL
);

-- change data type for cust_PhoneNumber
ALTER TABLE Customers MODIFY COLUMN cust_PhoneNumber BIGINT;

-- create address table
CREATE TABLE Address (
    add_ID INTEGER NOT NULL PRIMARY KEY,
    cust_ID INTEGER NULL,
    add_BuildingNumber INTEGER NULL,
    add_StreetName CHAR(50) NULL,
    add_City CHAR(50) NULL,
    add_PostCode CHAR(20) NOT NULL,
    add_Country CHAR(65) NOT NULL,
    FOREIGN KEY (cust_ID)
        REFERENCES Customers (cust_ID)
);

-- create treatments table
CREATE TABLE Treatments (
    trea_ID INTEGER NOT NULL PRIMARY KEY,
    trea_Name CHAR(25) NOT NULL
);

-- create appointments table
CREATE TABLE Appointments (
    appt_ID INTEGER NOT NULL PRIMARY KEY,
    cust_ID INTEGER NULL,
    trea_ID INTEGER NULL,
    appt_Date DATE NOT NULL,
    appt_Time TIME NULL,
    FOREIGN KEY (cust_ID)
        REFERENCES Customers (cust_ID),
    FOREIGN KEY (trea_ID)
        REFERENCES Treatments (trea_ID)
);

-- insert data for customers
INSERT INTO Customers 
	(cust_ID, cust_Title, cust_FirstName, cust_Surname, cust_Gender, cust_Age, cust_Email, cust_PhoneNumber) 
VALUES 
	(1, 'Miss', 'Joni', 'Sanders', 'Female', 19, 'jsanders@mail.com', 07045261418),
	(2, 'Mms', 'Falerina', 'Mazuret', 'Female', 74, 'FalerinaMazuret@mail.com', 0755552335),
    (3, 'Ms', 'Sammy', 'Smith', 'Female', 32, 'ssmith@mail.com', 07732087725),
    (4, 'Mrs', 'Annie', 'Sunshine', 'Female', 24, 'asunshine@mail.com', 89052301389),
    (5, 'Mms', 'Aya', 'Binet', 'Female', 53, 'AyaBinet@mail.com',0557598190),
    (6, 'Ms', 'Elle', 'Woods', 'Female', 27, 'Elle.Woods@mail.com', 07745751555),
    (7, 'Mrs', 'Hermione', 'Granger-Potter', 'Female', 64, 'mrs.granger.potter@mail.com', 07963974982),
    (8, 'Ms', 'Luna', 'Weasley', 'Female', 58, 'lweasley@mail.com', 07031626873);

-- insert data for address
INSERT INTO Address 
	(add_ID, cust_ID, add_BuildingNumber, add_StreetName, add_City, add_PostCode, add_Country ) 
VALUES 
	(1, 1, '59', 'Prospect Hill', 'Drighlington', 'BD11 1EW', 'UK'),
	(2, 2, '9', 'Rue Du Port', 'Pessac', '24230', 'France'),
    (3, 3, '51', 'Hampton Court Rd', 'Spetchley', 'WR5 8DN', 'UK'),
    (4, 4, '90', 'Telford Street', 'Bardsley', 'OL8 3GL', 'UK'),
    (5, 5, '19', 'Rue Mabley', 'Bordeaux', '33000', 'France'),
    (6, 6, '38', 'Wenlock Terrace', 'Petton', 'SY4 7BJ', 'UK'),
    (7, 7, '23', 'Holgate Road', 'Ramsey', 'CO12 7TH', 'UK'),
    (8, 8, '934', 'Radcliff Way', 'Woodley', 'RG5 4AZ', 'UK');

-- insert data for treatments
INSERT INTO Treatments
	(trea_ID, trea_Name)
VALUES
	(1, 'Visualisation'),
    (2, 'Relaxation'),
    (3, 'Regression'),
    (4, 'Inner Child'),
    (5, 'CBT'),
    (6, 'NLP'),
    (7, 'PMR'),
    (8, 'Suggestion');

-- insert data for appointments
INSERT INTO Appointments
	(appt_ID, cust_ID, trea_ID, appt_Date, appt_Time)
VALUES
	(1, 1, 4, '2024-09-30', '14:30:00'),
    (2, 2, 7, '2024-10-23', '10:15:00'),
    (3, 3, 4, '2024-07-02', '15:00:00'),
    (4, 4, 4, '2024-12-17', '10:15:00'),
    (5, 5, 1, '2024-09-17', '17:30:00'),
    (6, 6, 4, '2024-11-01', null),
    (7, 7, 6, '2024-09-24', '17:30:00'),
    (8, 8, 1, '2024-12-14', '10:15:00');

-- retrieve all data for each table
SELECT *
FROM Customers;

SELECT *
FROM Address;

SELECT *
FROM Treatments; 

SELECT *
FROM Appointments;

-- DATE_FORMAT Shows appointments in a more accessible format
SELECT cust_Surname, DATE_FORMAT(appt_Date, '%d %a %b') AS 'Formatted Appointment Date (2024)'
FROM Appointments
JOIN Customers
ON Appointments.cust_ID = Customers.cust_ID
ORDER BY appt_Date ASC;

-- LEFT() - Return the leftmost number of characters as specified (for confidentiality purposes)
SELECT cust_ID,
LEFT(cust_FirstName, 1) AS 'First Name Initial', 
LEFT(cust_Surname, 1) AS 'Surname Initial'
FROM Customers
ORDER BY cust_ID ASC;

-- LEFT() - concatenated the results to show in 1 column rather than 2 (for confidentiality purposes)
SELECT cust_ID,
CONCAT(LEFT(cust_FirstName, 1), 
LEFT(cust_Surname, 1)) 
AS 'Customer Initials'
FROM Customers
ORDER BY cust_ID ASC;

-- Inner join with order by and select to show the result of Appointments table
-- in order of date with surnames from Customers table
SELECT appt_ID, cust_Surname, appt_Date,  appt_Time
FROM Customers
INNER JOIN
    Appointments ON Appointments.cust_ID = Customers.cust_ID
ORDER BY appt_Date;

-- retrieve all customers in the UK (left join) with surnames
SELECT add_Country, cust_Surname
FROM Customers
LEFT JOIN
	Address ON Address.cust_ID = Customers.cust_ID
WHERE add_Country = 'UK';

-- Count the number of customers in a certain Country 
SELECT COUNT(add_Country) AS 'French_Customers'
FROM Address
WHERE add_Country = 'France';

-- retrieve all appointments in order
SELECT *
FROM Appointments
ORDER BY appt_Date;

-- List of all treatments and how many times they have been 
-- given to a customer in desc order to see most popular 
SELECT Treatments.trea_Name,
	COUNT(Appointments.trea_ID) AS treatments_recommended
FROM Appointments
INNER JOIN
	Treatments ON Appointments.trea_ID = Treatments.trea_ID
GROUP BY Appointments.trea_ID
ORDER BY treatments_recommended DESC;


-- Create table for procedure to show the total times used of each treatment
CREATE TABLE Top_Treatment (
    trea_Name VARCHAR(20),
    treatments_recommended INT
);

-- Create procedure to insert data into the Top_Treatment table to reduce chance of errors
DROP PROCEDURE IF EXISTS PROC_TopTreatment;

DELIMITER //

CREATE PROCEDURE PROC_TopTreatment()
BEGIN
	INSERT INTO Top_Treatment
	(trea_Name, treatments_recommended)
	SELECT Treatments.trea_Name, COUNT(Appointments.trea_ID) AS 'treatments recommended'
	FROM Appointments
	INNER JOIN Treatments
	ON Appointments.trea_ID=Treatments.trea_ID
	GROUP BY Appointments.trea_ID;
END //

DELIMITER ;

-- Call the procedure to insert data 
call hypnotherapy_crm.PROC_TopTreatment();

-- Show the data in descending order
SELECT *
FROM Top_Treatment
ORDER BY treatments_recommended DESC;

-- Show the data in descending order and return top value
SELECT 
	MAX(trea_Name) AS 'Most common treatment', 
	MAX(treatments_recommended) AS 'Amount of treatments'
FROM Top_Treatment;

-- Delete statement (if someone wants to cancel their appointment)  
DELETE FROM Appointments 
WHERE cust_ID = 6;

SELECT *
FROM Appointments; -- shows the updated table without specified row
    


