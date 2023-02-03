import random

def KiesWoord(woorden):
    woord = random.choice(woorden)
    return woord

def VraagLetter():
    letter = input("Kies 1 letter")
    if len(letter) > 1:
        print("Je kan maar 1 letter tegelijk kiezen")
    else:
        return letter

try:
    with open("woorden_eenvoudig.txt", "r") as file:
        content = file.read()
    woordenlijst = content.split('\n')
except:
    print('error with opening file')

woord = KiesWoord(woordenlijst)
letters = list(woord)
print(letters)
correctletters = ""

while True:
    letter = VraagLetter()
    for x in letters:
        if letter == x:
            correctletters+=letter
        else:
            continue
    print(correctletters)