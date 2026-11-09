import random

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
