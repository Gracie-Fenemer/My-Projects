# API key setup instructions are given to you in the instruction.txt file

#IMPORTS
# Import request for api
from lord_of_the_rings_sdk import LordOfTheRings
# API Key and url
api_key = # Your key here in ''
api = LordOfTheRings(api_key)
# Import additional module
import datetime
import pprint

#VARIABLES
#variable for numbered questions
number = range(1-4)
# Initialize score
score = 0

#FUNCTIONS
# Function to keep a running total of the correct answers
def points(score):
    score += 1 # Add 1 point to score for every correct answer
    return score
def goodbye(): # function with return
    print('Well, here at last, dear friends, on the shores of the Sea comes the end of our fellowship in Middle-earth. Go in peace! I will not say: do not weep; for not all tears are an evil.')
def questions(): # function with return
    print('There were 4 questions in this quiz...')

# This program allows the user to answer 4 quiz questions related to the Lord Of The Rings.
# For each correct answer, it connects to The One API and as a bonus provides the user with some interesting facts or information

# Welcome message and User identification
print('Welcome to this Lord of The Rings quiz! ') # first inbuilt funtion
user_name = input('What is your name? ') # user-input to refer back to throughout the application
print(f'Hi {user_name}')

# Datetime - returns todays date when called, in a specific layout of dd/mm/yyyy
today = datetime.datetime.now()
print('Todays date is: ' + str(today.strftime("%d/%b/%Y")))
print() #Tidy the console output


# Consent/interest with if/else and while loop with exit() function
interest = input('Do you like Lord of The Rings? Enter (y / meh)')
love_it = interest == ['y', 'yes', 'Y', 'YES', 'yeh']
not_love = interest == ['meh', 'm', 'no', 'nah', 'mah', 'idk']
if love_it:
    print(f'{user_name} welcome, welcome!')
if not_love:
    print(f'Sorry {user_name}, you will not enjoy this')
# for loop to do the quiz (or not) based on the previous answer
while interest == 'meh':
    print(f'You can go.')
    exit()
else:
    print(f'I am not sure what you put but here is question 1...')
print() #Tidy the console output

# QUIZ QUESTION 1
# First Question - with if/else, user input and getting the score
count_1 = 0
print(f'Q1: Who wrote the Lord of The Rings')
choices_q1 = ['Dr. Seuss', 'J.R.R. Tolkien', 'J.K. Rowling']
for number, word in enumerate(choices_q1): # For loop to return choices as a numbered list
    print(number+1, word)
while count_1 < 2 or q1 == 2 : # while loop to get multiple tries until the answer is correct
    q1 = int(input(f'Enter the number of your choice: '))
    if q1 == 2:
        print(f'Yes, Well done {user_name}!')
        resp = api.quote(the_id='5cd96e05de30eff6ebcce85b')
        quote_author = resp.json()['docs'][0]['dialog']
        pprint.pprint(f'A quote from J.R.R. Tolkien, The Return of the King: {quote_author}')
        # print()
        score = points(score)  # Update score by calling the function
        break
    else:
        print(f'Not quite, sorry!')
        count_1 = count_1 + 1

print(f'Next question...')
print() #Tidy the console output

# QUIZ QUESTION 2
# # Second question - includes returning values from list in a numbered list
count_2 = 0
print(f'Q2: Where does LOTR take place?')
choices_q2 = ['Shire', 'Spain', 'Middle-Earth']
for number, word in enumerate(choices_q2):
    print(number+1, word)
while count_2 < 2 or q2 == 3 : # while loop to get multiple tries until the answer is correct
    q2 = int(input(f'Enter the number of your choice: '))
    if q2 == 3:
        print(f'Hooray!')
        score = points(score)  # Update score by calling the function
        resp = api.quote(the_id='5cd96e05de30eff6ebcce9b9')  # API returning a piece of dialog
        quote_middle_earth = resp.json()['docs'][0]['dialog']
        pprint.pprint(f'A quote from The Lord of the Rings: The Two Towers: {quote_middle_earth}')
        print()
        break
    else:
        print(f'Uhh, no.')
        count_2 = count_2 + 1
print(f'Next question...')
print() #Tidy the console output

# QUIZ QUESTION 3
# # Third Question
count_3 = 0
print('Q3: Who made The One ring?')
choices_q3 = ['Sauron', 'Bilbo Baggins', 'Gollum']
for number, word in enumerate(choices_q3):
    print(number+1, word)
while count_3 < 2 or q3 == 1 : # while loop to get multiple tries until the answer is correct
    q3 = int(input(f'Enter the number of your choice: '))
    if q3 == 1: #api being used here to print name and race of a character within a string, to get more information about the answer (if correct)
        resp = api.character(the_id='5cd99d4bde30eff6ebccfea5')
        name_q3 = resp.json()['docs'][0]['name']
        race_q3 = resp.json()['docs'][0]['race']
        print(f'Yes, congrats! Did you know {name_q3} is a {race_q3}?')
        score = points(score)  # Update score by calling the function
        break
    else:
        print(f'Not exactly..')
        count_3 = count_3 + 1
print(f'Next question...')
print() #Tidy the console output

# QUIZ QUESTION 4
# Fourth question uses slice with a variable
best_character = 'legolas'
count_4 = 0
print(f'Q4: Unscramble this word: ' + str(best_character[::-1]))
choices_q4 = ['Gimli', 'Legolas', 'Gandalf']
for number, word in enumerate(choices_q4):
    print(number + 1, word)
while count_4 < 2 or q4 == 2 : # while loop to get multiple tries until the answer is correct
    q4 = int(input(f'Enter the number of your choice: '))
    if q4 == 2: #api being used here to print wiki Url from api for more information on the answer
        resp = api.character(the_id='5cd99d4bde30eff6ebccfd81')
        name_q4 = resp.json()['docs'][0]['name']
        wiki_url = resp.json()['docs'][0]['wikiUrl']
        print(f'Well done! If you want to know more about {name_q4} click here -> {wiki_url} !')
        score = points(score)  # Update score by calling the function
        break
    else:
        print(f'Hmm try again..')
        count_4 = count_4 + 1
print(f'Next question...')
print() #Tidy the console output

# QUIZ RESULTS
# Display final results and goodbye message
print(questions())
print(f'You\'re score is: {score}/4!') # call function and returns question string
if score == 4:
    print(f'YOU ARE AMAZING')
else:
    print(f'That\'s ok, I still appreciate you :)')
goodbye() # call function and returns the goodbye string

# END OF PROGRAM