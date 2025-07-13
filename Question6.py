numbers = []
n = int(input("Enter how many numbers you want in the tuple: "))
for i in range(n):
    num = int(input("Enter number " + str(i + 1) + ": "))
    numbers.append(num)

tup = tuple(numbers)

total = 0
for num in tup:
    total += num
average = total / len(tup)

sorted_list = list(tup)
for i in range(len(sorted_list)):
    for j in range(i + 1, len(sorted_list)):
        if sorted_list[i] > sorted_list[j]:
            temp = sorted_list[i]
            sorted_list[i] = sorted_list[j]
            sorted_list[j] = temp

if len(sorted_list) % 2 == 1:
    median = sorted_list[len(sorted_list) // 2]
else:
    mid1 = sorted_list[len(sorted_list) // 2 - 1]
    mid2 = sorted_list[len(sorted_list) // 2]
    median = (mid1 + mid2) / 2

max_count = 0
mode = sorted_list[0]
for i in range(len(sorted_list)):
    count = 0
    for j in range(len(sorted_list)):
        if sorted_list[i] == sorted_list[j]:
            count += 1
    if count > max_count:
        max_count = count
        mode = sorted_list[i]

print("Tuple:", tup)
print("Average:", average)
print("Median:", median)
print("Mode:", mode)