""" Doiraning elementlari quyidagi tartibda nomerlangan. 1-radius R, 2-diametr D=2*R, 3- uzunligi L=2piR,
 4-doiraning yuzasi S=PiR^2 Shu elementlardan bittasi beniganda qolganlarini topuvchi programma tuzilsin. pi=3.14"""
import math
pi=3.14
x=input("Qaysi emlementni kirit,oqchisiz(R/D/L/S): ")
if x=="R":
    r=float(input("Radiusni kiriting: "))
    print(f"Doira yuzi:{pi*r**2}. \nDoira uzunligi {2*pi*r}. \nDoira diametri {r*2}.\nDoira radiusi {r}")
elif x=="D":
    d=float(input("Diametrni kiriting: "))
    print(f"Doira yuzi {(d/2)**2*pi}.\nDoira uzunligi{pi*d}.\nDoira diametri {d}. \nDoira radiusi {d/2}")
elif x=="S":
    s=float(input("Yuzini kiriting: "))
    print(f"Doira yuzi {s}.\nDoira uzunligi {math.sqrt(s/pi) *2*pi}.\nDoira diametri {math.sqrt(s/pi) *2}. \nDoira radiusi {math.sqrt(s/pi)}")
elif x=="L":
    l=float(input("Uznligini kiriting: "))
    print(f"Doira yuzi {(l/(2*pi))**2*pi}.\nDoira uzunligi{l}.\nDoira diametri {l/pi}. \nDoira radiusi {l/(2*pi)}")
else:
    print(0)