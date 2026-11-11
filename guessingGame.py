import random

words = ["counter Strike", "silksong", "cairn", "deadlock", "expedition 33"]

print("Good luck with guessing the game!")

word = random.choice(words).lower()

print("Guess the characters")

guessed = set()
turns = 12


while turns > -1:
    counter = 0

    if turns == 0:
            print("You lose")
            print("The word was: " + word)
            break 
    
    guess = input("\nGuess a character: ").lower()

    if len(guess) < 1:
        print("Please enter a character")
        continue
    if len(guess) > 1:
        print("Please only enter a single character")
        continue
    if guess in guessed:
        print("you already guessed " + guess)
        continue

    guessed.add(guess)

    for char in word:
        if char in guessed:
            counter += 1
    if counter == len(word):
        print("You win")
        print("The word is: " + word)
        break

    for char in word:
        if char in guessed:
            print(char, end=" ")
        else:
            print("_", end=" ")

    if guess not in word:
        turns -= 1
        print("\nWrong")
        combined_reply = ("You have " + str(turns) + " more guesses")
        print(combined_reply)
            
