def Polindrom(soz):
   
    if len(soz) <= 1:
        return True

    if soz[0] != soz[-1]:
        return False

    return Polindrom(soz[1:-1])

# Test qilish
soz = str(input("So'zni kiriting: "))

print(Polindrom(soz))

