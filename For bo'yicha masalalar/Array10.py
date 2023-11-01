"""
n ta elementdan tashkil topgan massiv berilgan. Dastlab massiv elementlari orasidan juftlarini indekslari
o'sish tartibida chiqaruvchi, keyin massiv elementlari orasidan toqlarini indekslari kamayish tartibida chiqaruvchi programma tuzilsin.
Massiv elementlar 4 5 7 8 6 9
Natija: 4 8 6 9 7 5
"""

a=list(map(int,input().split()))
s=[]
d=0
h=0
x=[]
y=[]
z=[]
for i in a:
    if i%2==0:
        s.append(a.index(i))
        d=d+1
        x.append(i)
        s.sort()
        x.sort()
    elif i%2==1:
        z.append(a.index(i))
        h = h + 1
        y.append(i)
        z.sort()
        z.reverse()
        y.sort()
        y.reverse()
print("Indexlari:")
print(*s)
print("Juft sonlar soni: " )
print(d)
print("Massiv ichidagi juft sonlar: ")
print(*x)
print("Indexlari:")
print(*z)
print("Toq sonlar soni: " )
print(h)
print("Massiv ichidagi toq sonlar: ")
print(*y)