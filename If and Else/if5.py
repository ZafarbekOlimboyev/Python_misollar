"""Uchta butun son berilgan. Shu sonlar orasidan nechta musbat va manfiy son borligini aniqlovchi programma tuzilsin."""
a=int(input("Birinchi sonni kiriting: "))
b=int(input("Ikkinchi sonni kiriting: "))
c=int(input("Uchinchi sonni kiriting: "))
s=0
s1=0
if a>0:
    s=s+1
if a<0:
    s1=s1+1
if b>0:
    s=s+1
if b<0:
    s1=s1+1
if c>0:
    s=s+1
if c<0:
    s1=s1+1
print(f" {s} ta musbat va {s1} ta manfiy son bor.")