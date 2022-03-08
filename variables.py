#  basics of variables
def length(name):
    return len(name)

name = "lav"
print(f'name: {name}  length:{length(name)} ')
name = "Priyanshi"

# "id(<variable_name>)" 
#     it will return the address of the object which is 
#     stored in the ref. variable

print("This is the id of name[0]", id(name[0]))
print('name: ', name[0], id(name), type(name), length(name))
name = 43
print('name: ', type(name), id(name))

