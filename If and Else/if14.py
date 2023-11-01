"""Uchta son berilgan. Shu sonlarni avval kichigini keyin kattasini ekranga chiqaruvchi programma tuzilsin."""
a=float(input("Birinchi sonni kiriting: ")) # Bu joyda Data typeni float qilib qo`yganimni sababi masala shartida son deyilgan
b=float(input("Ikkinchi sonni kiriting: ")) # Ya`ni ixtiyoriy son butun deyilmagan shu sababdan float qilganman
c=float(input("Uchinchi sonni kiriting: "))

if a>b>=c or a>c>=b:
    if b>c:
        print(f"Kichigi {c}, Kattasi {a}")
    elif c>b:
        print(f"Kichigi {b}, Kattasi {a}")
    else:
        print(f"Kichigi {c}, Kattasi {a}")
elif a>=b>c or a>=c>b:
    if b>c:
        print(f"Kichigi {c}, Kattasi {a}")
    elif c>b:
        print(f"Kichigi {b}, Kattasi {a}")
    else:
        print(f"Kichigi {c}, Kattasi {a}")
elif b>a>=c or b>c>=a:
    if a>c:
        print(f"Kichigi {c}, Kattasi {b}")
    elif c>a:
        print(f"Kichigi {a}, Kattasi {b}")
    else:
        print(f"Kichigi {c}, Kattasi {b}")
elif b>=a>c or b>=c>a:
    if a>c:
        print(f"Kichigi {c}, Kattasi {b}")
    elif c>a:
        print(f"Kichigi {a}, Kattasi {b}")
    else:
        print(f"Kichigi {c}, Kattasi {b}")
elif c>a>=b or c>b>=a:
    if a>b:
        print(f"Kichigi {b}, Kattasi {c}")
    elif b>a:
        print(f"Kichigi {a}, Kattasi {c}")
    else:
        print(f"Kichigi {a}, Kattasi {c}")
elif c>=a>b or c>=b>a:
    if a>b:
        print(f"Kichigi {b}, Kattasi {c}")
    elif b>a:
        print(f"Kichigi {a}, Kattasi {c}")
    else:
        print(f"Kichigi {a}, Kattasi {c}")
else:
    print("Uchta son ham teng.")
