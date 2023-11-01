""" Koordinatalar tekisligida butun son berilgan. Agar nuqta koordinata boshida yotsa, O chiqarilsin. Agar nuqta OX yoki
 OY oqlarida joylashsa mos holda 1 va 2 chiqarilsin. Agar nuqta koordinata oqida oylashmasa 3 chiqarilsin."""
x=int(input("X ni qiymatini kiriting: "))
y=int(input("Y ni qiymatini kiriting: "))
if x==0 and y==0:
    print("O")
elif x==0:
    print(1)
elif y==0:
    print(2)
else:
    print(3)