"""
n ta elementdan tashkil topgan massiv berilgan (n juft son). Dastlab massiv elementlari orasidan toq indekslilarini o'shish tartibida
keyin juft indekslilarini kamayish tartibida chiqaruvchi programma tuzilsin. A[1], A[3], A[5]. A[6], A[4] A[2], A[0] Shart operatori ishlatilmasin.
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
d.reverse()
print(*d,*y)