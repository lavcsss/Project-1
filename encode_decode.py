# Encryption and Decryption using unicode

"""
Encryption
"""
def encode(text, shift):
    cipher_text = ""
    for i in text:
        # if i == " ":
        #     y = ord(i) + 65 + shift
        #     cipher_text += chr(y)
        #     continue
        x = ord(i) + shift
        if x == 127:
            x = 95
        cipher_text += chr(x)
    print(f"Encrpted message: {cipher_text}")

def decode(cipher_text, shift):
    text = ""
    for i in cipher_text:
        # if i == chr(32 + 65 + shift):
        #     y = ord(i) - 65 - shift
        #     text += chr(y)
        #     continue
        if i == chr(95):
            z = 127 - shift
            text += chr(z)
            continue
        x = ord(i) - shift
        text += chr(x)
    print(f"decrypted message: {text}")


should_continue = True
while should_continue:
    direction = input("Type \"encode\" for encryption or \"decode\" for decryption \n").lower()
    text = input("Enter your message \n").lower()
    shift = int(input("Enter the shift value\n"))
    shift = shift % 97                # if shift is larger than our list
    if direction == "encode":
        encode(text=text, shift=shift)
    if direction == "decode":
        decode(cipher_text=text, shift=shift)
    result = input("Type \"yes\" for continue or \"no\" for exit.\n")
    if result == "no":
        should_continue = False
        print("Good Bye")
# else:
#     print("Please enter the correct keyword")