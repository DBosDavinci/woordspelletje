import random

def KiesWoord(woorden):
    woord = random.choice(woorden)
    return woord

def VraagLetter():
    letter = input("Kies 1 letter\n")
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

correctletters = []
for x in range(len(letters)):
    correctletters.append("_")
print(letters,"\n",correctletters)

fouten = 0

while True:
    if fouten >= 10:
        print("Je hebt teveel fout geraden, start opnieuw.")
        quit()
    else:
        letter = VraagLetter()
        if letter not in letters:
            print("deze letter zit niet in het woord!")
            fouten+=1
            print(f"Je zit nu op {fouten}/10 fouten")
        elif letter in correctletters:
            print("Je hebt deze letter al eerder geraden!")
        else:
            for x in range(len(letters)):
                if letter == letters[x]:
                    correctletters[x] = letter
                else:
                    continue
        print("".join(correctletters))

        if correctletters == list(woord):
            print("Je hebt het woord geraden!")
            quit()
