"""
n ta elementdan tashkil topgan massiv berilgan. Massiv elementlarini quyidagicha chiqaruvchi programma tuzilsin.
A[0], A[1], A[n-1], A[n-2], A[3], A[4], A[n-3], A[n-4],...
"""
a=list(map(int,input().split()))
b=a.copy()
b.reverse()
k=0
f=[]
while k <len(b)/2-1:
    f.append(a[k])
    h=k+1
    f.append(a[h])
    f.append(b[k])
    f.append(b[h])
    k=k+2
f.append(a[(len(a)//2-1)])
f.append(a[(len(b)//2)])
print(*f)