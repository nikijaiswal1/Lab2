all_students = []
cricket = []
football = []

total = int(input("Enter total number of students: "))
for i in range(total):
    roll = input("Enter roll number of student " + str(i + 1) + ": ")
    all_students.append(roll)

n1 = int(input("Enter number of students who play cricket: "))
for i in range(n1):
    roll = input("Enter roll number of cricket player " + str(i + 1) + ": ")
    cricket.append(roll)

n2 = int(input("Enter number of students who play football: "))
for i in range(n2):
    roll = input("Enter roll number of football player " + str(i + 1) + ": ")
    football.append(roll)

both = []
only_one = []
neither = []

for roll in all_students:
    in_cricket = False
    in_football = False

    for c in cricket:
        if roll == c:
            in_cricket = True
            break

    for f in football:
        if roll == f:
            in_football = True
            break

    if in_cricket and in_football:
        both.append(roll)
    elif in_cricket or in_football:
        only_one.append(roll)
    else:
        neither.append(roll)

print("Students who play both sports:", both)
print("Students who play only one sport:", only_one)
print("Students who play neither sport:", neither)