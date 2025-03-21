import random

player_name = input("What is your name? ").lower().capitalize()
print(f"Good luck '{player_name}'!\n")

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']
selected_word = random.choice(words)

print("Here is the random word:")
for char in selected_word:
    print("_")
print("")
print("You have 12 chances to guess the correct characters.\n")

def word_guessing_game():
    chances = 12
    guessed_chars = []
    loop = 0
    while chances > 0:
        if set(guessed_chars) == set(selected_word):
            return f"Congratulations, '{player_name}'. You won the game.\n The word is '{selected_word}'.\n"
        
        loop += 1
        if loop > 1:
            print(f"You still have '{chances}' chances.")
        guess = input("guess a character: ").lower()

        if len(guess) > 1:
            print(f"Please enter only ONE character. You entered {len(guess)} characters.\n")
            continue
        if guess.isalpha() == False:
            print(f"{guess} is not an alphabetic character. Please enter an ALPHABETIC character.\n")
            continue

        chances -= 1
        if guess in list(selected_word):
            guessed_chars.append(guess)
            for char in selected_word:
                if char in guessed_chars:
                    print(char)
                else:
                    print("_")
            print("")
        else:
            print("Wrong.\n")
    return "Game over.\n"

print(word_guessing_game())
    