for i in range(1,9):
    for j in range(0, 9-i):
        print(end=" ")
    for k in range(0, i):
        print("*", end=" ")
    print()