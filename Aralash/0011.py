"""
2-max
n(2≤n≤100)n(2≤n≤100) ta elementdan iborat butun sonli massiv berilgan. Massivning ikkinchi eng katta elementini aniqlang.

Chiquvchi ma'lumotlar:
Massivning ikkinchi eng katta elementini chiqaring.

input:5
      1 5 2 3 4
output:
       4
input:6
       3 5 5 2 2 3
output:5
"""
a=int(input())
b=list(map(int,input().split()))
b.pop(b.index(max(b)))
print(max(b))