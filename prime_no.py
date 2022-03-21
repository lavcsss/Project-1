#Write your code below this line 👇

def prime_checker(number):
    count =2
    while(count <= number / 2):
        if (number % count == 0):
            flag = 1
            break
        else:
            flag =0
        count += 1
    if (flag == 1):
        print("It's not a prime number.")
    else:
        print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)