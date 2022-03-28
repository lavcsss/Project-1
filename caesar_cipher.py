# Caesar cipher
from turtle import position


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:                # checks for the letters only and encrypt them
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:               # doesn't encrypt symbols/numbers/spaces
            end_text += char
    print(f"{cipher_direction}d message is {end_text}")
while 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26              # if shift is larger than our list

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    chance = input("Type \"yes\" to continue or \"no\" to exit\n")
    if chance == "no":
        exit()
    if chance == "yes":
        continue
    else:
        print("Please type \"yes or no\"")

    # def encode(plain_text, shift_amount):
    #     cipher_text = ""
    #     for i in plain_text:
    #         position = alphabet.index(i)
    #         new_position = position + shift_amount
    #         cipher_text += alphabet[new_position]
    #     print(f"Encrpyted message is :{cipher_text}")


    # def decode(cipher_text, shift_amount):
    #     plain_text = ""
    #     for i in cipher_text:
    #         position = alphabet.index(i,25)
    #         old_position = position - shift_amount
    #         plain_text += alphabet[old_position]
    #     print(f"Decrypted message is :{plain_text}")
    # if direction == "encode":
    #     encode(plain_text = text, shift_amount = shift)
    # if direction == "decode":
    #     decode(cipher_text = text, shift_amount = shift)
