"""
n ta elementdan tashkil topgan massiv berilgan. Massiv elementlari orasidan juftlarini indekslari
kamayish tartibida chiqaruvchi va ularning sonini chiqaruvchi programma tuzilsin. Massiv elementlar: 457869 Natija: 6 8 4 juftlar soni = 3
"""
a=list(map(int,input().split()))
s=[]
d=0
x=[]
for i in a:
    if i%2==0:
        s.append(a.index(i))
        d=d+1
        x.append(i)
        s.sort()
        s.reverse()
        x.sort()
        x.reverse()
print("Indexlari:")
print(*s)
print("Toq sonlar soni: " )
print(d)
print("Massiv ichidagi juft sonlar: ")
print(*x)