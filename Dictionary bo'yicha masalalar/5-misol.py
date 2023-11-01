"""
N butun soni berilgan. 1 dan N gacha bo’lgan sonlarni key sifatida,
ularning kvadratini value sifatida dictionary da saqlaydigan dastur
yozing.
"""
n=int(input())
x={}
for i in range(1,n+1):
    x[i]=i**2
print(x)