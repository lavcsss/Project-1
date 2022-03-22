import random
# Hangman game 
# Take a list for of words.

guessed_word = []
words = ["player", "happy", "racer", "coder"]
word = random.choice(words)
print(word)
for i in range(0,len(word)):
    guessed_word.append("_")
print(guessed_word)
for i in word:
    guess_letter = input("\nGuess the letter:")
    if word.count(guess_letter) > 0:
        for j in range(0, len(word)):
            if guess_letter == word[j]:
                guessed_word[j] = word[word.index(guess_letter)]
        else:
            pass
    print(guessed_word)
else:
        print("Better luck next time")
