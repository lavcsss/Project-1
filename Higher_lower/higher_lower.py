from replit import clear
import random

from arts import logo, vs
from game_data import data



def compare_person(personal_1, current_score):
    print(logo)
    personal_2 = random.choice(data)
    print(f'Compare_A:  {personal_1["name"]}, {personal_1["description"]}, {personal_1["country"]}')
    print(vs)
    print(f' Against_B:  {personal_2["name"]}, {personal_2["description"]}, {personal_2["country"]}')
    choice_ = input("Who has more followers? Type 'A' or 'B' : ").upper()

    if choice_== "A":
        if personal_1["follower_count"] > personal_2["follower_count"]:
            current_score = (current_score + 1)
            clear()
            print(f"You're right! Current Score: {current_score}")
            compare_person(personal_1=personal_2, current_score=current_score)
        else:
            clear()
            print(f"Sorry that's wrong, Final Score : {current_score}")
    
    else:
        if personal_2["follower_count"] > personal_1["follower_count"]:
            current_score = (current_score + 1)
            clear()
            print(f"You're right! Current Score: {current_score}")
            compare_person(personal_1=personal_2, current_score=current_score)
        else:
            clear()
            print(f"Sorry that's wrong, Final Score : {current_score}") 


flag = True
score = 0
personal_1 = random.choice(data)


compare_person(personal_1=personal_1, current_score=score)
