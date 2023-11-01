"""
 n ta elementdan tashkil topgan massiv berilgan. Massiv elementlarini quyidagicha chiqaruvchi programma tuzilsin.

A[0], A[n-1], A[1], A[n-2], A[2], A[n-3],...
"""
a=list(map(int,input().split()))
b=a.copy()
b.reverse()
k=0
f=[]
while k <len(b)/2:
    f.append(a[k])
    f.append(b[k])
    k=k+1
print(*f)