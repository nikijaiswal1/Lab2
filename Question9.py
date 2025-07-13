import random

numbers = set()

while len(numbers) < 5:
    num = random.randint(1, 100)
    numbers.add(num)

print("Initial set with random values:", numbers)

while len(numbers) < 10:
    num = int(input("Enter a number to add to the set: "))
    numbers.add(num)

print("Set with 10 unique elements:", numbers)

smallest = min(numbers)
largest = max(numbers)

numbers.remove(smallest)
numbers.remove(largest)

print("Set after removing smallest and largest:", numbers)
