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
        update_display += 1

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
woord_lijst = ["aarde", "informatica","informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografiewaardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk", "glorieus", "mantis garnaal", "skelet", "wolk","spongebob", "python", ]

chosen_word=list(random.choice(woord_lijst))

blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)

update_display = 0

# controleren of het een letter is
def get_valid_letter():
    while True:
        guess = input("Raad een letter? ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Voer alleen een letter in!")

# het starten van het spel (introductie)

print(HANGMAN[update_display])
print(f"je speelt galgje.\n{blank}")
guess = get_valid_letter()
making_a_guess()
print(HANGMAN[update_display])
print(''.join(blank_list))

# Standen (winnen, verliezen, nog een keer raden)
while update_display < 6:
    if blank_list == chosen_word:
        print("Je hebt gewonnen glorieuze KING!")
        break
    guess = get_valid_letter()
    making_a_guess()
    print(HANGMAN[update_display])
    print(''.join(blank_list))
    
if update_display == 6:
    print("GAME OVER YOU TWAT.")
    print(f"Het woord was {chosen_word}")