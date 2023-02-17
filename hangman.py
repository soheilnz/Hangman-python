import random

words = ["python","dictionary","laptop","hangman","secret"]
word = random.choice(words)
MAX_GUESSES = 6
guesses = []
finish = False

while not finish:
    for letter in word:
        if letter.lower() in guesses:
            print(letter,end=" ")
        else:
            print("_",end = " ")
    print(" ")

    guess = input(f"allowed guesses: {MAX_GUESSES}, guess a word: ")
    guesses.append(guess.lower())
    
    if guess.lower() not in word.lower():
        MAX_GUESSES -= 1
        if MAX_GUESSES == 0:
            break
    
    finish = True
    for letter in word:
        if letter.lower() not in guesses:
            finish = False

if finish:
    print(f"you found word! it was {word}")
else:
    print(f"you lose! the word was {word}")