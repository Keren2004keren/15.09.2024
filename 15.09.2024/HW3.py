# START
# 1
x: int = int(input("Enter a positive whole number: "))
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(x - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# 2
x: int = int(input("Enter a positive whole number: "))
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(x - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# STOP
