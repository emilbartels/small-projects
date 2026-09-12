import random

words = ["cherry", "brownie", "banana", "faceit", "computer", "counter strike"]

word = random.choice(words)

print("Hello welcome to TGGGE aka. The Greatest Guessing Game Ever")

guesses = []
turns = 12

numberofletters = len(word)
fillupguess = []
i = 0


#Making the empty list which the user will fill
while i  < numberofletters:
    fillupguess.append("_")
    i = i + 1

while turns > 0:
    character = input("What character do you guess: ")
    if character in word:
        print("You guessed correctly!")

        #Logic for filling up guessing array
        for i, letter in enumerate(word):
            if letter == character:
                fillupguess[i] = character
    
            
        print("Here is the guesses word so far: " + "".join(fillupguess))

        if "".join(fillupguess) == word:
            print("CONGRATS YOU GUESSED THE WHOLE WORD CORRECT!")
            break
    else:
        turns = turns - 1
        if turns == 0:
            print("You didn't guess the word in 12 tries so you are dead")
        else:
            print("You unfortunatly guessed wrong. You have " + str(turns) + " guesses left.")
            print("So far you have guessed: " + "".join(fillupguess))
        
    
#print("".join(fillupguess)) 
#print(word)