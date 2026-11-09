import random

<<<<<<< HEAD
#Create a list of words and randomly select one.
#Initialize variables to store guessed characters and remaining attempts.
#Display the word using underscores for unguessed characters.
#Accept a character from the user.
#Check whether the character exists in the word.
#Continue until the word is guessed or all attempts are exhausted.
#Display the result.

words = ["counter Strike", "silksong", "cairn", "deadlock", "expedition 33"]

name = input("What is your name?")
print("Good luck with guessing the game!")

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed + 1

        print()

        if guesses == len(word):
            print("You win")
            print("The word is: ", word)
            break

        guess = input("Guess a character: ").lower()

        if len(guess) != 1:
            print("Please enter a single character")
            continue

        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong")
            combined_reply = ("You have" + str(turns) + " more guesses")
            print(combined_reply)
            if turns == 0:
                        print("You lose")
                        print("The word was: ", word)
=======
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
>>>>>>> edeb9b38263e20e5e48d5a6586a5e1a895a42ca5
