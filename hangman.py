import random

print("Welcome to HangMan!")
Continue = input("q to quit,r for rules, else to start/continue!")

wordsList = []

with open('words.txt', 'r') as f:
    for line in f:
        for word in line.split():
            wordsList.append(word)

chosenWord = random.choice(wordsList)
print(chosenWord)

wordLength = len(chosenWord)
dashesExtra = wordLength - 4
dashes = ["_", "_", "_", "_"]

for i in range(dashesExtra):
    dashes.append("_")
print(' '.join(dashes))


def guessing():
    hearts = 6
    print(hearts, "guesses left!")
    letter = input("Guess!")
    count = chosenWord.count(letter)
    print(count)

    if letter not in chosenWord:
        hearts = hearts - 1
        print(hearts, "guesses left!")
    elif hearts == 0:
        print("you lose!")
        return

    elif letter in chosenWord and count > 1:
        print("working")
        return
    else:
        position = (chosenWord.find(letter))
        dashes[position] = letter
        print(' '.join(dashes))


if Continue == "r":
    print("1.) Don't add a space before your guess")
    print("2.) Guess must be in lowercase")
    print("3.) You will be told if its a double letter!")
    print("4.) We don't allow word guesses D:")
else:
    guessing()

'''
chosenWord = random.choice(wordsList)
print(chosenWord)

wordLength = len(chosenWord)
dashesExtra = wordLength - 4
dashes = ["_", "_", "_", "_"]
    

for i in range(dashesExtra):
    dashes.append("_")
print(' '.join(dashes))
'''

while Continue != "q":
    guessing()

f.close()
