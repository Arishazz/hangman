
import random


print("Welcome to HangMan!")
Continue = input("q to quit,r for rules, else to start/continue!")

wordsList = []


    
with open('words.txt','r') as f:
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
    letter = input("Guess a letter!")
    if letter not in chosenWord:
         print("""
         +---+
         |   |
         O   |
             |
             |
             |
     =========
     """)


    else:
        # position = (chosenWord.find(letter))
        # dashes[position] = letter

        remaining = chosenWord.count(letter)
        position = 0
        while (remaining!=0):
            position = chosenWord.find(letter, position)
            dashes[position]= letter
            remaining -= 1
        
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







