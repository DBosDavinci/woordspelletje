import random

try:
    with open("woorden_eenvoudig.txt", "r") as file:
        content = file.read()
    woordenlijst = content.split('\n')
except:
    print('error with opening file')

print(random.choice(woordenlijst))

def KiesWoord(woordenlijst:list):
    random.choice(woordenlijst)