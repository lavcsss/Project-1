import random
import hangman_arts
import hangman_words
# Hangman game 
# Take a list for of words.
print(hangman_arts.logo)
lives = -1
flag = False
guessed_word = []
# words = ["player", "happy", "racer", "coder"]
word = random.choice(hangman_words.words)
print(word)
for i in range(0,len(word)):
    guessed_word.append("_")
print(guessed_word)
while not flag:
    guess_letter = input("\nGuess the letter:")
    if word.count(guess_letter) > 0:
        for j in range(len(word)):
            if guess_letter == guessed_word[j]:
                print(f"You already gussed {guess_letter}")
            if guess_letter == word[j]:
                guessed_word[j] = word[word.index(guess_letter)]
    else:
        print("Better luck next time")
        print(hangman_arts.stages[lives])
        lives -= 1
    print(guessed_word)
    if "_" not in guessed_word:
        flag = True
        print("You win")
    if lives == -8:
        flag = True
        print("You lose")
