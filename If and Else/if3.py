"""Butun son berilgan. Agar, berilgan son musbat bo`lsa, 1 ga oshiring, agar manfiy bo`lsa 2 ga kamaytiring.
 Agar 0 ga teng bo`lsa, 10 ni o`zlashtirsin. Hosil bo`lgan sonni ekranga chiqaruvchi programma tuzilsin."""

a=int(input("Sonni kiriting: "))
if a>0:
    print(a+1)
elif a<0:
    print(a-2)
else:
    print(10)