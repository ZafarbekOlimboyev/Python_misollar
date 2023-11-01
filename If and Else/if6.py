"""Ikkita butun son berilgan. Shu sonlardan kattasini aniqlovchi programma tuzilsin."""
a=int(input("Birinchi sonni kiriting: "))
b=int(input("Ikkinchi sonni kiriting: "))
if a>b:
    print(f" {a} katta.")
elif b>a:
    print(f"{b} katta.")
else:
    print("Ikkalasi teng")