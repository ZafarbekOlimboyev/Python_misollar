"""A va B butun sonlari berilgan. Agar o`zaro teng bo`lmasa, A va B o`zgarvchilarini yig`indisi o`zlashtirilsin.
Agar teng bo`lsa, 0 o`zlashtirilisn. A va B ning qiymati ekranga chiqarilsin."""
a=int(input("A sonni kiriting: "))
b=int(input("B sonni kiriting: "))
if a!=b:
    print(f"Yig`indi {a+b} ga teng. A {a} ga teng, B {b} ga teng.")
else:
    print(f"0. A {a} ga teng, B {b} ga teng.")