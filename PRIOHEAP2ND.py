from heapq import heappush, heappop

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print("This is the list of elements in the Queue:", fruits)
print("")

heappop(fruits)

print("This is the list of elements in the Queue after heappop:", fruits)