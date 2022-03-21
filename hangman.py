import random
# Hangman game 
# Take a list for of words.


words = ["player", "happy", "racer", "coder"]
word = random.choice(words)
print(word)
for i in range(0,len(word)):
    print("_", end= " ")
for i in word:
    guess_letter = input("\nGuess the letter:")
    if word.count(guess_letter) > 0:
        print(word[word.index(guess_letter)])
        
    else:
        print("Better luck next time")
