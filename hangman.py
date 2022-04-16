
import random

print("Welcome to HangMan!")
# rules: dont space before u enter a letter, make sure ur letter is lowercase.
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
        print("loserrr") # change to draw
    else:
         #position = (chosenWord.find(letter))
        position = ([pos for pos, char in enumerate(chosenWord) if char == letter])
        
        print(' '.join(dashes))
    
      


guessing()
        
   
        


f.close()







