import random

print('Welcome to "Word Guessing Game"')
player_name = input("What's your name? ").lower().capitalize()
print("")

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']
selected_word = random.choice(words)

print("Here's the selected random word (The word is in lowercase):")
for char in selected_word:
    print("-")
print("")

chances = 12
print(f'Dear "{player_name}", You have 12 chances to guess the correct characters.')

def word_guessing_game():
    global chances
    guessed_chars_correct = []
    guessed_chars_all = []
    loop = 0
    while chances > 0:
        if set(guessed_chars_correct) == set(selected_word):
            return f"Congratulations, '{player_name}'. You won the game.\nThe word is '{selected_word}'.\n"
        
        if loop > 0:
            print(f"Guessed characters: {guessed_chars_all}")
            print(f"Your chances: {chances}")
            
        loop += 1
        guess = input("guess a character: ").lower()

        if len(guess) > 1:
            print(f"Please enter only ONE character. You entered {len(guess)} characters.\n")
            continue
        if guess.isalpha() == False:
            print(f'"{guess}" is not an alphabetic character. Please enter an ALPHABETIC character.\n')
            continue

        chances -= 1
        guessed_chars_all.append(guess)
        if guess in list(selected_word):
            guessed_chars_correct.append(guess)

        for char in selected_word:
            if char in guessed_chars_correct:
                print(char)
            else:
                print("-")
        print("")

    return "Unfortunately, you lost the game.\nGame over.\n"

print(word_guessing_game())
