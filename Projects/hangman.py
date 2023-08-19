"""
Hangman Game

There might be some new things that you don't recognize here, so don't be afraid to search up something you don't understand.
You can also always message us if you have any questions!
"""

word = "apple"
dashes = list("-" * len(word))  # You can "multiply" strings which creates one string with the text repeated as many times as it's multiplied. list() converts a string into a list, splitting up each character
guessed = []
guesses_left = 3
done = False

print("Welcome to our Hangman Game!\n")
print((f"Word to guess: {''.join(dashes)}"))  # join is a string method that joins a list together into a string, and whatever you put into the string is what each element will be seperated by (in this case, nothing)

while not done:
    letter = input("Guess a letter: ")

    if len(letter) > 1 or not letter.isalpha():  # Checks if the number of letters are greater than 1 or if it isn't in the alphabet
        print("You should input only 1 letter.\n")
        continue

    elif letter in guessed:  # Checks if the letter is in the guessed list (means the user already guessed it before)
        print("You already guessed that letter!\n")
        continue

    if letter in word:  # Checks if the letter is not in the word
        print(f"{letter} is in the word!")
        guessed.append(letter)

        index = 0  # Counter to keep track of the indexes
        for l in word:
            if l == letter:  # Checks if the letter in the word is the same as the letter the user guessed
                dashes[index] = letter  # Changes the dash to the letter the user guessed at the same index
            index += 1  # Adds to the index

    else:
        print(f"{letter} is not in the word.")
        guesses_left -= 1  # Brings guesses_left down by one since they misguessed the letter

    print((f"\nWord to guess: {''.join(dashes)}"))  # Joins the list of dashes back into a string to print

    if guesses_left <= 0:  # Checks if they have reached 0 guesses left
        print(f"You've ran out of guesses. The word was {word}.")
        done = True
    if "-" not in dashes:  # Checks if there is no more dashes (means they guessed all the letters)
        print("Congratulations! You got the word!")
        done = True
