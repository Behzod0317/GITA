import random

def takrorlanmas_raqamlar(n, m):
    if n > m:
        raise ValueError("'n' soni 'm' dan katta bo'lmasligi kerak!!!")

    takrorlanmas_raqam = random.sample(range(1, m + 1), n)
    return takrorlanmas_raqam

n = int(input("n : "))
m = int(input("m : "))

natija = takrorlanmas_raqamlar(n, m)
print("Natija:")
print(*natija)
