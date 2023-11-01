"""Ikkita butun son berilgan. Shu sonlarning avval kattasini keyin kichigini ekranga chiqaruvchi
programma tuzilsin."""
a=int(input("Birinchi sonni kiriting: "))
b=int(input("Ikkinchi sonni kiriting: "))
if a>b:
    print(f"{a} {b}")
elif b>a:
    print(f" {b}  {a}")
else :
    print("Ikkalasi teng.")