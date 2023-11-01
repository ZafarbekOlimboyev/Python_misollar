"""
Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligini teskari tartibda chiqaradigan dastur tuzing

Masalan: Ismlar: john, alice, bob Natija: bob, alice, john
"""
a=input().split(",")
b=[]
for i in a:
    b.append(i + ",")
b.reverse()
print(*b)