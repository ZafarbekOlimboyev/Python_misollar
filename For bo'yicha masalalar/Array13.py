"""
N ta elementdan tashkil topgan massiv berilgan (n toq son).Massiv elementlar orasidan
quyidagilarini chiqaruvchi programma tuzilsin. A[n-1], A[n-3],... A[1]. Shart operatori ishlatilmasin.
"""
a=list(map(int,input().split()))
d=[]
z=0
for o in a:
    z=z+1
for i in range(1,z,2):
    c=a[i]
    d.append(c)
d.reverse()
print(*d)