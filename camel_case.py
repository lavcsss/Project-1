# Changing the name to CamelCase

def format_fun(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Please enter the full name"
    first_name = f_name[:1].upper() + f_name[1:len(f_name)].lower()
    last_name = l_name[:1].upper() + l_name[1:len(l_name)].lower()
    return(first_name + " " + last_name)

name = input("Enter your name").split(" ")
print(format_fun(name[0], name[1]))
