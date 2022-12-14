from thirdqueues import Stack

lifo = Stack("1st", "2nd", "3rd")
print("This is the number of current queues:",len(lifo))
print("")

for element in lifo:
    print(element)

print("")
print("This is the number of current queues:",len(lifo))