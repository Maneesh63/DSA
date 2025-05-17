def pattern(n):
    for i in range(n):
        for j in range(n, i, -1):
            print(j, end="")
        print()

print(pattern(8))
