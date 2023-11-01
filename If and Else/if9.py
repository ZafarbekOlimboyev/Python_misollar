"""A va B haqiqiy sonlari berilgan. Shu sonlarni shunday o`zgartirish kerakki, A son kichik B son katta bo`lsin.
A va B ning qiymati ekranga chiqarilsin."""
a=float(input("A sonni kiriting: "))
b=float(input("B sonni kiriting: "))
if a>b:
    a,b = b,a
    print(f"A son {a} B son {b}.")
elif b>a:
    print(f"A son {a} B son {b}.")
else:
    print(f"A son {a-1} B son {b}") #  Masala shartida O`zgartiring deyilgan Almashtiring deyilmagan shu sababdan a dan 1 ayirib qoydim.