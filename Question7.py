coordinates = []
n = int(input("Enter how many coordinates you want to enter: "))
for i in range(n):
    x = int(input("Enter x" + str(i + 1) + ": "))
    y = int(input("Enter y" + str(i + 1) + ": "))
    coordinates.append((x, y))

straight_line = True

x1 = coordinates[0][0]
y1 = coordinates[0][1]
x2 = coordinates[1][0]
y2 = coordinates[1][1]

for i in range(2, len(coordinates)):
    x3 = coordinates[i][0]
    y3 = coordinates[i][1]
    
    area = (x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))
    
    if area != 0:
        straight_line = False
        break

if straight_line:
    print("The points lie on a straight line.")
else:
    print("The points do not lie on a straight line.")