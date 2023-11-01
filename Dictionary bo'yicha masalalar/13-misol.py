"""
A va B nomli ro’yxatlar berilgan. Ularni bir lug’atga aylantiradigan
dastur tuzing. Bunda A ro’yxatdagi ma’lumotlar key sifatida, B
ro’yxatdagi ma’lumotlar value sifatida qabul qilinsin.
"""
a=input("A ni kiriting: ").split()
b=input("B ni kiriting: ").split()
m={}
i=0
while i<len(a):
    m[a[i]]=b[i]
    i +=1
print(m)