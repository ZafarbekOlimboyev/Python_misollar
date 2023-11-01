"""
 n ta elementdan tashkil topgan massiv va K butun soni berilgan (1 < K < n). Massiv elementlari orasidan indeksi K ga
 karralilarini chiqaruvchi programma tuzilsin. Shart operatori ishlatilmasin.
"""
a = list(map(int, input().split()))
k = int(input())
c = []
h=k
# List element index out of range
while h < len(a):
    j= a[h]
    c.append(j)
    h=h+k
print("Indexlarni K ga karralilari quyidagicha: ")
print(*c)


