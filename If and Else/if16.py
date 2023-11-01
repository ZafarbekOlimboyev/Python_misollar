"""A, B, C haqiqiy sonlari berilgan. Agar berilgan sonlar o'sish tartibida berilgan bo'lsa,
 sonlarni ikkilantiring, aks holda sonlarni ishorasi o'zgartirilsin. A, B, C ning qiymatlari ekranga chiqarilsin"""
a=float(input("A sonni kiriting: "))
b=float(input("B sonni kiriting: "))
c=float(input("C sonni kiriting: "))

if c>b>a:
    print(f"A = {a*2}, B = {b*2}, C ={c*2}")
else:
    print(f"A = {a * (-1)}, B = {b * (-1)}, C ={c * (-1)}")