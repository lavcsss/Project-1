import random
import hangman_arts
# Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import words

# Hangman game 
print(hangman_arts.logo)
lives = -1
flag = False
guessed_word = []

# words = ["player", "happy", "racer", "coder"]
word = random.choice(words)

#Create blanks
for i in range(0,len(word)):
    guessed_word.append("_")
print(f"{' '.join(guessed_word)}")

while not flag:
    guess_letter = input("\nGuess the letter:").lower()
    if guess_letter in guessed_word:
        print(f"You already gussed {guess_letter}")
    if word.count(guess_letter) > 0:

        #Check guessed letter
        for j in range(len(word)):
        # If the user has entered a letter they've already guessed, print the letter and let them know.
            if guess_letter == word[j]:
                guessed_word[j] = word[word.index(guess_letter)]
    else:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess_letter} is not correct letter. Better luck next time")
        print(hangman_arts.stages[lives])
        lives -= 1
    print(f"{' '.join(guessed_word)}")
    if "_" not in guessed_word:
        flag = True
        print("You win")
    if lives == -8:
        flag = True
        print("You lose")
        print(f" Ans is {word}")
