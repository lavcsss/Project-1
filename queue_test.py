queue = []
while 1:
    queue.append(input("Enter element in the queue"))
    num = input("press \"e\" if no more elements are left to enter")   # <\"\"> escaping a string
    if (num == "e"):
        break
    else:
        pass

print(queue)
operation = input ("Press D to delete the element from the queue")
if operation == "D":
    last_index = 