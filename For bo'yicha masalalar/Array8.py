"""
 n ta elementdan tashkil topgan massiv berilgan. Massiv elementlari orasidan toqlarini indekslari o'sish
 tartibida chiqaruvchi va ulaming sonini chiqaruvchi programma tuzilsin. Massiv elementlar: 457869 Natija: 5 7 9 toqlar soni = 3
"""
a=list(map(int,input().split()))
s=[]
d=0
x=[]
for i in a:
    if i%2==1:
        s.append(a.index(i))
        d=d+1
        x.append(f"{i},")
print("Indexlari:")
print(*s)
print("Toq sonlar soni: " )
print(d)
print("Massiv ichidagi toq sonlar: ")
print(*x)