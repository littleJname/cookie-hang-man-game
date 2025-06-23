#galgje de spel van hangen en woorden raden
#import voor het willekeurig kiezen van een woord

import random

# voor het raden van een letter
def making_a_guess():
    x = 0
    global update_display
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    if not correct_guess:
        print(f"Geen {guess}, sorry.")
        incorrect_guesses.append(guess.lower())
        update_display += 1

# functie om te controleren of invoer alleen letters bevat
def is_valid_letter(input_str):
    return len(input_str) == 1 and input_str.isalpha()

#hangman tekeningen 
HANGMAN = (
    """
 --+---+--
 |   |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 --+---+--
 |   |
 |   O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 --+---+--
 |   |
 |   O
 |  ---
 |   |
 |   
 |   
 |     
----------
""",
"""
 --+---+--
 |   |
 |   O
 | /---
 |   
 |   
 |   
 |    
----------
""",
"""
 --+---+--
 |    |
 |    O
 |  /---/
 |   
 |   
 |   
 |      
----------
""",
"""
 --+---+--
 |    |
 |    O
 |  /---/
 |    |
 |   
 |   
 |     
----------
""",
"""
 --+---+--
 |   |
 |   O
 | /---/
 |   |
 |  |
 |  | 
 |     
----------
""",
"""
 --+---+--
 |   |
 |   O
 | /---/
 |   |
 |   |
 |  | |
 |  | |
 |  
----------
""")

#woordenlijst
woord_lijst = ["aarde", "informatica", "golrieus", "mantis garnaal", "spongebob",  "python", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie",
"waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk" ]

chosen_word = list(random.choice(woord_lijst))

blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)

update_display = 0
incorrect_guesses = []

# het starten van het spel (introductie)

print(HANGMAN[update_display])
while True:
    if incorrect_guesses:
        guess = input(f"je speelt hangman.\n{blank}\nVerkeerde letters: [{', '.join(incorrect_guesses)}]\nRaad een letter? ")
    else:
        guess = input(f"je speelt hangman.\n{blank}\nRaad een letter? ")
    if is_valid_letter(guess):
        break
    else:
        print("Voer alleen een letter in, geen cijfers of andere tekens")

making_a_guess()
print(HANGMAN[update_display])
print(''.join(blank_list))
if incorrect_guesses:
    print(f"Verkeerde letters: [{', '.join(incorrect_guesses)}]")

# Standen (winnen, verliezen, nog een keer raden)
while update_display < 6:
    if blank_list == chosen_word:
        print("Je hebt gewonnen glorieuze KING!")
        break
    
    while True:
        if incorrect_guesses:
            guess = input(f"Doe het nog een keer\nVerkeerde letters: [{', '.join(incorrect_guesses)}]\nRaad een letter: ")
        else:
            guess = input("Doe het nog een keer\nRaad een letter: ")
        if is_valid_letter(guess):
            break
        else:
            print("Voer alleen één letter in, geen cijfers of andere tekens!")
    
    making_a_guess()
    print(HANGMAN[update_display])
    print(''.join(blank_list))
    if incorrect_guesses:
        print(f"Verkeerde letters: [{', '.join(incorrect_guesses)}]")

if update_display == 6:
    print("GAME OVER YOU TWAT.")
    print(f"Het woord was {chosen_word}")
