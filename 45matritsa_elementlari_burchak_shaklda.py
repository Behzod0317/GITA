import random

m = 10
a = [[random.randint(0, 9) for _ in range(m)] for _ in range(m)]

for row in a:
    print(*row)

print("\n")

for i in range(m):
    for j in range(m - i):
        print(a[i][j], end=" ")
    print()
    
    for j in range(i + 1, m):
        print(a[j][m - i - 1], end=" ")
    print()
