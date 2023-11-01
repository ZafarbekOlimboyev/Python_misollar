"""
n ta elementdan tashkil topgan massiv berilgan (n juft son).
Massiv elementlar orasidan quyidagilarini chiqaruvchi programma tuzilsin. A[0], A[2], A[4],... Shart operatori ishlatilmasin.
"""
a=list(map(int,input().split()))
d=[]
z=0
for o in a:
    z=z+1
for i in range(0,z,2):
    c=a[i]
    d.append(c)
print(*d)