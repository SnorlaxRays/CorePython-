n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        if k % 2 != 0:
            print(" ", end="")
        else:
            print("*", end="")
    if i % 2 == 0:
        for m in range(i + 1):
            if m % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
    elif i % 2 != 0:
        for m in range(i + 1):
            if m % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")

    print()
