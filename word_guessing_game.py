import random

name = input("What is your name? ")
print(f"Good luck '{name}'!")

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print("Here is the chosen word:")
for char in word:
    print("_")
print("")
print("You have got 12 guesses.")

