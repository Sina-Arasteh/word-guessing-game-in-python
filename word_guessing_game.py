import random

name = input("What is your name? ").lower().capitalize()
print(f"Good luck '{name}'!\n")

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print("Here is the random word:")
for char in word:
    print("_")
print("")
print("You have got 12 guesses.\n")

print(f"{word}\n")

def word_guessing_game():
    turns = 12
    guesses = []
    loop = 0
    while turns > 0:
        if set(guesses) == set(word):
            return f"Congratulations, '{name}'. You win the game.\n The word is '{word}'.\n"
        
        loop += 1
        if loop > 1:
            print(f"You still have got '{turns}' guesses.")
        guess = input("guess a character: ").lower()

        if len(guess) > 1:
            print(f"Please enter only ONE character. You entered {len(guess)} characters.\n")
            continue
        if guess.isalpha() == False:
            print(f"{guess} is not an alphabetic character. Please enter an ALPHABETIC character.\n")
            continue

        turns -= 1
        if guess in list(word):
            guesses.append(guess)
            for char in word:
                if char in guesses:
                    print(char)
                else:
                    print("_")
            print("")
        else:
            print("Wrong.\n")
    return "Game over.\n"

print(word_guessing_game())
    
