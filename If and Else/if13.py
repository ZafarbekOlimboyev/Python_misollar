"""Uchta son berilgan. Shu sonlarni o`rtachasini (ya`ni katta va kichigi sonlar o`rtasidagi son) ni aniqlovchi programma tuzilsin."""
a=float(input("Birinchi sonni kiriting: ")) # Bu joyda Data typeni float qilib qo`yganimni sababi masala shartida son deyilgan
b=float(input("Ikkinchi sonni kiriting: ")) # Ya`ni ixtiyoriy son butun deyilmagan shu sababdan float qilganman
c=float(input("Uchinchi sonni kiriting: "))

if a>b>c or c>b>a:
    print(f" O`rtachasi {b}")
elif b>a>c or c>a>b:
    print(f" O`rtachasi {a}")
elif a>c>b or b>c>a:
    print(f" O`rtachasi {c}")
else:
    print("Siz kiritgan sonlarni o`rtachasini aniqlashni iloji yo`q.")