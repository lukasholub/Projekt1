"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukáš Holub
email: lucas.r.holub@gmail.com
discord: lukasholub94
"""
#import of sys for terminating the programe in case of wrong credentials
import sys
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
separator = "-" * 60

#variable so that the number of texts can be any number
number_of_texts = len(TEXTS)

#dictionary with registered users
registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

#searching within the login credentials dictionary
if input_username in registered_users and registered_users[input_username] == input_password:
    print(separator)
    print("Welcome to the app,", input_username)
else: 
    print("Unregistered user, terminating the program...")
    sys.exit()
print(f"We have {number_of_texts} texts to be analyzed")
print(separator)

#choosing the text by integer input
input_choosing_text = int(input("Enter a number between 1 and 3 to select: "))

#making sure the entered number logically corresponds to the list
input_choosing_text -= 1

#creating a list for all the words we work with
clean_words = []
for word in TEXTS[input_choosing_text].split():
    clean_word = word.strip(",.?!-")
    clean_words.append(clean_word)
number_of_words = len(clean_words)
print(separator)
print(f"There are {number_of_words} words in the selected text")

#list of titlecase words
number_of_titlecase_words = []
for word in clean_words:
    if word.istitle():
        number_of_titlecase_words.append(word)
print(f"There are {len(number_of_titlecase_words)} titlecase words")

#list of uppercase words
number_of_uppercase_words = []
for word in clean_words:
    if word.isupper():
        number_of_uppercase_words.append(word)
print(f"There are {len(number_of_uppercase_words)} uppercase words")

#list of lowercase words
number_of_lowercase_words = []
for word in clean_words:
    if word.islower():
        number_of_lowercase_words.append(word)
print(f"There are {len(number_of_lowercase_words)} lowercase words")

#list of the sum of all the numbers
sum_of_all_numbers = []
for word in clean_words:
    if word.isnumeric():
        sum_of_all_numbers.append(int(word))
print("The sum of all the numbers:",sum(sum_of_all_numbers))
print(separator)
separator = "-" * 40
print("LEN | OCCURRENCES |     NR.")
print(separator)

#dictionary to store word lengths and their occurrences
word_lengths = {}

#iterate over each word in clean_words
for word in clean_words:
    length = len(word)

#increase the count for the current word length
    word_lengths[length] = word_lengths.get(length, 0) + 1

#print graph
for length in sorted(word_lengths.keys()):
    occurrences = word_lengths[length]
    print(f"{length:2}  | {'*' * occurrences:15}  | {occurrences}")
