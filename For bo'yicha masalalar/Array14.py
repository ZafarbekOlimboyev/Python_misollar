"""
N ta elementdan tashkil topgan massiv berilgan. Dastlab massiv elementlari orasidan juft indekslilarini keyin toq indekslilarini chiqaruvchi
programma tuzilsin. A[0], A[2], A[4]... A[1], A[3], A[5]... Shart operatori ishlatilmasin. n ta elementdan tashkil topgan massiv berilgan.
Dastlab massiv elementlari orasidan juft indekslilarini keyin toq indekslilarini chiqaruvchi programma tuzilsin.
A[0], A[2], A[4]... A[1], A[3], A[5]... Shart operatori ishlatilmasin.
"""
a=list(map(int,input().split()))
d=[]
y=[]
z=0
for o in a:
    z=z+1
for i in range(1,z,2):
    c=a[i]
    d.append(c)
for i in range(0,z,2):
    c=a[i]
    y.append(c)
print(*y,*d)