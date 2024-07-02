1. Firstly open the config.py file. Input your MySQL Workbench user, host and password in the designated quotes
2. Open the db_utils.py file (follow instructions here) and import mysql.connector
3. Open app.py and follow instructions to install Flask
4. After all modules are imported then run app.py and run client_main at the same time and fill in the information accordingly in the console.

* Building an app for a zoo visitors.
* They can search up all the different animals in the zoo by their name or all information on 1 specific animal.
* They can add animals that may be missing, or that they would like to see.

 <u>config.py</u>
 <br /> This file stores the user's private information in order for the MySQL database to be connected to this project.
 You need to insert your user, host and password where specified. <br /> The information is stored in a variable and is called in the db_utils.py 
 file, this means no private information can be seen by the client.
 
<u>db_utils.py</u>
<br /> This file has the utilities that contains functions and a class that handles database connections, perform/run queries and manage data transformations. 
<br /> This imports needed for this document to be able to run. These are mysql.connector and the config file.
<br /> To import mysql.connector you can either do a *'pip install mysql-connector-python'* in your terminal or if there is a red squiggle underlining the words mysql.connector you can click install and wait a moment.
<br /> The config.py file holds your private login/user information for MySQL so that when connecting, the database is available.

<u>app.py</u>
<br /> This is the api. It allows multiple software applications to communicate with each other and return/add data. Also known as the backend server.#
<br /> The imports needed for this are Flask and another file from within the project, db_utils. 
In your terminal type *'pip install Flask'*. The rest (jsonify and requests) will them be imported once the code is run. 
<br /> If it is not working, they should have a red squiggle underneath, and you can hover over it and install that way.


<u>client_main.py</u> 
<br /> This has the functions to interact with your backend server.
<br /> This file serves as the primary script that runs the client-side application to interact with the backend server. It handles user interaction, fetches data from the server, and displays the information to the user.
<br /> This file needs 2 imports. Requests should already be imported into the project. Json if there is a red squiggle, hover over and install.


<u>Database in MySQL</u>
<br /> Attached in the GitHub branch is the SQL database that will need to be opened and run once in your MySQL database. This is mandatory for this app to run.


<u>Expected Output</u>
<br /> The client is visiting the zoo and would like to use the app to see what animals are in it, compared to physically at the zoo.
<br /> The client sees the list and sees that it is missing one of the animals, so using the information they know/find at the zoo, they add it!
<br /> They now want to check the information is correct or show a friend or family member the new animal only from the app.