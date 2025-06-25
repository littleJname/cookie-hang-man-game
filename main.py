#galgje de spel van hangen en woorden raden
#import voor het willekeurig kiezen van een woord

import random

# voor het raden van een letter
def making_a_guess():
    x = 0
    global update_display
    goede_keuze = False
    for letter in gekozen_woord:
        if keuze.lower() == gekozen_woord[x]:
            blank_list[x] = keuze.lower()
            goede_keuze = True
        x += 1
    if not goede_keuze:
        print(f"Geen {keuze}, sorry.")
        foute_keuze.append(keuze.lower())
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
 | |---
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
 |  |---|
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
 |  |---|
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
 | |---|
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
 | |---|
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

gekozen_woord = list(random.choice(woord_lijst))

# fouten antwoorden en het raden van een woord
blank = ""
for letter in gekozen_woord:
    blank += "_"
blank_list = list(blank)

update_display = 0
foute_keuze = []

# het starten van het spel (introductie)

print(HANGMAN[update_display])
while True:
    if foute_keuze:
        keuze = input(f"je speelt hangman.\n{blank}\nVerkeerde letters: [{', '.join(foute_keuze)}]\nRaad een letter? ")
    else:
        keuze = input(f"je speelt hangman.\n{blank}\nRaad een letter? ")
    if is_valid_letter(keuze):
        break
    else:
        print("Voer alleen een letter in, geen cijfers of andere tekens")

making_a_guess()
print(HANGMAN[update_display])
print(''.join(blank_list))
if foute_keuze:
    print(f"Verkeerde letters: [{', '.join(foute_keuze)}]")


# Standen (winnen, verliezen, nog een keer raden)
while update_display < 6:
    if blank_list == gekozen_woord:
        print("Je hebt gewonnen glorieuze KING!")
        break
    
    while True:
        if foute_keuze:
            keuze = input(f"Doe het nog een keer\nVerkeerde letters: [{', '.join(foute_keuze)}]\nRaad een letter: ")
        else:
            keuze = input("Doe het nog een keer\nRaad een letter: ")
        if is_valid_letter(keuze):
            break
        else:
            print("Voer alleen één letter in, geen cijfers of andere tekens")


# verkeerde letters laten zien
    making_a_guess()
    print(HANGMAN[update_display])
    print(''.join(blank_list))
    if foute_keuze:
        print(f"Verkeerde letters: [{', '.join(foute_keuze)}]")

if update_display == 6:
    print("GAME OVER YOU TWAT.")
    print(f"Het woord was {gekozen_woord}")
