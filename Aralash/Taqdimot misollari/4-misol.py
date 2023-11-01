"""
Standart kiruvchi ma’lumotdan sonlarni o’qib olib, ushbu sonlarning
raqamlarini teskari tartibda chiqaruvchi dastur tuzing. Masalan:
Sonlar: 102 346 5897
Natija: 201 643 7985
"""
a=input().split()
b=[]
for i in range(len(a)):
    d=a[i][-1::-1]
    b.append(d)
print(*b)
