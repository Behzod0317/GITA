
def Yigindini_topuvchi(son):
    summa = 0
    for i in range(1, son):
        if son % i == 0:
            summa += i
    return summa

N = int(input("N : "))

dost_sonlar = []
for i in range(2, N + 1):
    j = Yigindini_topuvchi(i)
    if j > i and Yigindini_topuvchi(j) == i:
        dost_sonlar.append((i, j))

print(*dost_sonlar)



