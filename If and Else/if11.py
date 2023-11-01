"""A va B butun sonlari berilgan. Agar o`zaro teng bo`lmasa, A va B sonlarining kattasi o`zlashtirilsin.
Agar teng bo`lsa, 0 o`zlashtirilisn. A va B ning qiymati ekranga chiqarilsin."""
a=int(input("A sonni kiriting: "))
b=int(input("B sonni kiriting: "))
if a!=b:
    if a>b:
        print(f"Kattasi {a} . A {a} ga teng, B {b} ga teng.")
    else:
        print(f"Kattasi {b} . A {a} ga teng, B {b} ga teng.")
else:
    print(f"0. A {a} ga teng, B {b} ga teng.")