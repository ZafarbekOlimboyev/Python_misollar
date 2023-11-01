"""
Yangi lug'at yaratish uchun quyidagi lug'atlarni birlashtirish uchun
dastur tuzing:
Example: dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
n=int(input("Nechta lug'at yaratilsin: "))
x={}
z=0
for i in range(1,n+1):
    m=input(f"{i}-Lug'at elementlarini kiriting(1-kalit so'zi, 2-lug'ati 3-kalit so'z, 4-lug'ati va h.k).Masalan:(1 20 2 20 3 30 4 40): ").split()
    while z<len(m):
        x[m[z]]=m[z+1]
        z+=2
    z=0
print(x)
