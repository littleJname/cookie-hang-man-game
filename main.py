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
            blank = ["_"] * len(chosen_word)
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
word_list = ["aarde", "informatica", "golrieus", "pauw bidsprinkhaan garnaal", "grass", "skelet", "schaduw", "wolk", "paars", "spongebob", "roblox", "mango", "corny", "pyhton" ]

chosen_word = list(random.choice(word_list))

blank = "_" * len(chosen_word)

update_display = 0

# het starten van het spel (introductie)

print(HANGMAN[update_display])
guess = input(f"je speelt hangman.\n{blank}\nRaad een letter? ")
making_a_guess()
print(HANGMAN[update_display])
print(''.join(blank))

# Standen (winnen, verliezen, nog een keer raden)
while update_display < 6:
    if blank == chosen_word:
        print("Je hebt gewonnen glorieuze KING!")
        break
    guess = input("Doe het nog een keer ")
    making_a_guess()
    print(HANGMAN[update_display])
    print(''.join(blank))

if update_display == 6:
    print("GAME OVER YOU TWAT.")