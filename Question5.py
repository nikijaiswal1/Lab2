lst = []
size = int(input("Enter how many elements you want in the list: "))
for i in range(size):
    num = int(input("Enter element " + str(i + 1) + ": "))
    lst.append(num)

result = []
for i in range(len(lst)):
    n = lst[i]
    prime = True
    if n <= 1:
        prime = False
    else:
        j = 2
        while j * j <= n:
            if n % j == 0:
                prime = False
                break
            j = j + 1
    if i % 2 == 0 or prime:
        result.append(n)

print("Filtered list (even indexes or prime numbers):", result)