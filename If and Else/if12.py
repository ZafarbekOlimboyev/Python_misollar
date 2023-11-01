"""Uchta son berilgan. Shu sonlarning kichigini aniqlovchi programma tuzilsin."""
a=float(input("Birinchi sonni kiriting: ")) # Bu joyda Data typeni float qilib qo`yganimni sababi masala shartida son deyilgan
b=float(input("Ikkinchi sonni kiriting: ")) # Ya`ni ixtiyoriy son butun deyilmagan shu sababdan float qilganman
c=float(input("Uchinchi sonni kiriting: "))
if a>=b>c or b>=a>c or b>a==c or a>b==c:
    print(f"Kichigi {c} ga teng.")
elif a>=c>b or c>=a>b or a>c==b or c>a==b:
    print(f"Kichigi {b} ga teng.")
elif c>=b>a or b>=c>a or c>b==a or b>c==a:
    print(f"Kichigi {a} ga teng.")
else:
    print("Uchta son ham teng.")