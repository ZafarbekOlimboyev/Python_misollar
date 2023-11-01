"""Uchta butun son berilgan. Shu sonlarni ikkitasi o'zaro teng, qolgan bittasini tartib raqami aniqlansin."""
a=int(input("Birinchi sonni kiriting: "))
b=int(input("Ikkinchi sonni kiriting: "))
c=int(input("Uchinchi sonni kiriting: "))
if a==b:
    print("Tartib raqami 3")
elif a==c:
    print("Tartib raqami 2")
elif c==b:
    print("Tartib raqami 1")
else:
    print("Ikkita son o`zaro teng emas.")