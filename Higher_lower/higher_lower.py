from replit import clear
import random

from arts import logo, vs
from game_data import data
"""
    There is some mess in the code  please review it later.
"""

################################# "Definition based Solution" ####################################
def random_account():
    """
        Returns the random account
    """
    return random.choice(data)

def format_data(account):
    """
        Format the data in particular form
    """
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return account_name, account_des, account_country

def guess_ ():
    """
        Returns the user guess
    """
    return input("Who has more followers? Type 'A' or 'B' : ").upper()

def compare_person(personal_1, personal_2, current_score):
    if personal_1["follower_count"] > personal_2["follower_count"]:
        current_score = (current_score + 1)
        clear()
        print(f"You're right! Current Score: {current_score}")
        personal_2 = random_account()
        compare_person(personal_1=personal_2, current_score=current_score)
    else:
        clear()
        print(logo)
        print(f"Sorry that's wrong, Final Score : {current_score}")    
     

def game():
    score = 0
    print(logo)
    personal_1 = random_account()
    print(f"Compare A : {format_data(personal_1)}")
    print(vs)
    personal_2 = random_account()
    print(f"Against B: {format_data(personal_2)}")
    choice_ = guess_()
    while personal_1 == personal_2:
        personal_2 = random_account()
    if choice_== "A":
        compare_person(personal_1=personal_1, personal_2=personal_2)
    
    else:
        compare_person(personal_1=personal_2, personal_2=personal_1)



game()



################################# "First Approach" ####################################

# def compare_person(personal_1, current_score):
#     print(logo)
#     personal_2 = random.choice(data)
#     print(f'Compare_A:  {personal_1["name"]}, {personal_1["description"]}, {personal_1["country"]}')
#     print(vs)
#     print(f' Against_B:  {personal_2["name"]}, {personal_2["description"]}, {personal_2["country"]}')
#     choice_ = input("Who has more followers? Type 'A' or 'B' : ").upper()

#     if choice_== "A":
#         if personal_1["follower_count"] > personal_2["follower_count"]:
#             current_score = (current_score + 1)
#             clear()
#             print(f"You're right! Current Score: {current_score}")
#             compare_person(personal_1=personal_2, current_score=current_score)
#         else:
#             clear()
#             print(f"Sorry that's wrong, Final Score : {current_score}")
    
#     else:
#         if personal_2["follower_count"] > personal_1["follower_count"]:
#             current_score = (current_score + 1)
#             clear()
#             print(f"You're right! Current Score: {current_score}")
#             compare_person(personal_1=personal_2, current_score=current_score)
#         else:
#             clear()
#             print(f"Sorry that's wrong, Final Score : {current_score}") 


# flag = True
# score = 0
# personal_1 = random.choice(data)


# compare_person(personal_1=personal_1, current_score=score)

