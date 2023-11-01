"""Sonlar oqida uchta A, B, C nuqtalar berilgan. A nuqtaga eng yaqin nuqta va ular orasidagi masofa topilsin."""
a=float(input("A nuqtani kiriting: ")) # Bu joyda Data typeni float qilib qo`yganimni sababi masala shartida son deyilgan
b=float(input("B nuqtani kiriting: ")) # Ya`ni ixtiyoriy son butun deyilmagan shu sababdan float qilganman
c=float(input("C nuqtani kiriting: "))
d=abs(a-b)
e=abs(a-c)
if d>e:
    print(f"A nuqtaga eng yaqini C nuqta va ular orasidagi masofa {e} ga teng.")
elif d<e:
    print(f"A nuqtaga eng yaqini B nuqta va ular orasidagi masofa {d} ga teng.")
else:
    print(f"A nuqtadan ikkit anuqta ham teng uzoqlikda. Ular orqasidagi masofa {e} ga teng")