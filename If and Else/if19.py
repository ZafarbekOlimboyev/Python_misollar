"""To`rtta butun son berilgan. Shu sonlarni uchtasi o'zaro teng, qolgan bittasini tartib raqami aniqlansin."""
a=int(input("Birinchi sonni kiriting: "))
b=int(input("Ikkinchi sonni kiriting: "))
c=int(input("Uchinchi sonni kiriting: "))
d=int(input("To`rtinchi sonni kiriting: "))
if a==b==d:
    print("Tartib raqami 3")
elif a==c==d:
    print("Tartib raqami 2")
elif c==b==d:
    print("Tartib raqami 1")
elif a==b==c:
    print("Tartib raqami 4")
else:
    print("Ikkita son o`zaro teng emas.")