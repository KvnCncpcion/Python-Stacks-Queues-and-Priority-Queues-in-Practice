from scndqueues import Queue

fifo = Queue("1st", "2nd", "3rd")
print("This is the number of current queues:",len(fifo))
print("")

for element in fifo:
    print(element)

print("")
print("This is the number of current queues:",len(fifo))