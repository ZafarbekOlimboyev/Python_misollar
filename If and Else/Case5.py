"""A, B haqiqiy va amal butun soni berilgan. A va B sonlan ustida arifmetik amallar bajaruvchi
progaramma tuzilsin. amal quyidagi qiymatlarni qabul qiladi: 1-qo'shish, 2-ayinish, 3-bo'lsh, 4-ko'paytirish"""

a=float(input("A sonini kiriting: "))
b=float(input("B sonini kiriting: "))
c=int(input("Amalni kiriting (1-qo'shish, 2-ayinish, 3-bo'lsh, 4-ko'paytirish): "))
if c==1:
    print(f"{a} + {b} = {a+b}")
elif c==2:
    print(f"{a} - {b} = {a - b}")
elif c==3:
    print(f"{a} : {b} = {a / b}")
elif c==4:
    print(f"{a} * {b} = {a * b}")
else:
    print(0)
