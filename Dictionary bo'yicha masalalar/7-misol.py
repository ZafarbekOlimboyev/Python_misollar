"""
N butun soni berilgan. 1 dan N gacha bo’lgan toq sonlarni o’zida
jamlovchi lug’at dasturini tuzing. Bunda key sifatida saqlashi kerak
bo’lgan ma’lumotlar toq sonning tartib raqami bo’lsin, value sifati toq
sonni o’zi sifatida saqlab borsin.
"""
n=int(input())
x={}
s=1
for i in range(1,n,2):
    x[s]=i
    s+=1
print(x)