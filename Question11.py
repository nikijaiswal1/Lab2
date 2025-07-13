n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)
unique_numbers = set(numbers)
sorted_unique_numbers = sorted(unique_numbers)
print("Sorted list without duplicates:")
print(sorted_unique_numbers)
