"""
Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligini alifbo tartibida chiqaradigan dastur tuzing.
"""
a=input().split(",")
b=[]
for i in a:
    b.append(i + ",")
b.sort()
print(*b)