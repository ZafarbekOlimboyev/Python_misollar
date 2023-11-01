""" Uchta son berilgan. Shu sonlarning yig`indisi eng katta bo`ladigan ikkitasini ekranga chiqaruvchi programma tuzilsin."""
a=float(input("Birinchi sonni kiriting: ")) # Bu joyda Data typeni float qilib qo`yganimni sababi masala shartida son deyilgan
b=float(input("Ikkinchi sonni kiriting: ")) # Ya`ni ixtiyoriy son butun deyilmagan shu sababdan float qilganman
c=float(input("Uchinchi sonni kiriting: "))

d=max(a,b,c)
if d==a:
    print(f"{max(b,c)} va {a}")
elif d==b:
    print(f"{max(a,c)} va {b}")
else:
    print(f"{max(a,b)} va {c}")