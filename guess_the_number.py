import random
print("Welcome to Number Guessing game")
print("I'm thinking of a number between 1 to 100.")
level = input("Choose the difficulty level. Type 'easy' or 'hard': ")
if level == "easy":
    chances = 10
else:
    chances = 5

num = random.randint(1,100)
# print(num)

while(chances > 0):
    print(f"You have {chances} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess > num:
        print("Too high")
    elif guess < num:
        print("Too low")
    elif guess == num:
        print(f"You win the number is {num}.")
        exit()
    else:
        print("Invalid input")
    chances -= 1
print(f"You are out of chances. You lose {num}"  )