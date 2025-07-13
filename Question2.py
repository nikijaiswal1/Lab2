n1 = int(input('Enter the required numbers for list one: '))
l1 = []
i = 0
while i < n1:
    l1.append(int(input("Enter numbers: ")))
    i += 1
n2 = int(input('Enter the required numbers for list two: '))
l2 = []
i = 0
while i < n2:
    l2.append(int(input("Enter number")))
    i += 1
merged = []
i = 0
while i < len(l1):
    if l1[i] not in l2:
        merged.append(l1[i])
    i += 1
i = 0
while i < len(l2):
    if l2[i] not in l1:
        merged.append(l2[i])
    i += 1
print("Merged without common:", merged)

