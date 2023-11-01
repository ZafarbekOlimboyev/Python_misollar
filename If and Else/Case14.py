"""
 Tengtomonli uchburchakning elementlari quyidagi tartibda nomerlangan. 1-tomoni a, 2-ichki chizilgan aylananing radiusi a-√3/6, 3- tashqi
 chizilgan aylananing radiusi R₁ =2*R, 4-yuzasi S=a√3/4 Shu elementlardan bittasi berilganda qolganlarini topuvchi programma tuzisin
"""
import math
b=input("Elementni kiriting (A/R1/R2/S): ")
if b=="A":
    a=float(input("Tomonini kiriting: "))
    print(f"Teng tomonli uchburchakning ichki chizilgan aylana radiusi{a*math.sqrt(3)/6}")
    print(f"Teng tomonli uchburchakning tashqi chizilgan aylana radiusi{(a*math.sqrt(3)/6)*2}")
    print(f"Teng tomonli uchburchakning yuzi {a**2*math.sqrt(3)/4}")
elif b=="R1":
    a=float(input("R1 ni kiriting: "))
    print(f"Teng tomonli uchburchakning ichki chizilgan aylana radiusi{a}")
    print(f"Teng tomonli uchburchakning tashqi chizilgan aylana radiusi{a*2}")
    print(f"Teng tomonli uchburchakning yuzi {(6*a/math.sqrt(3))*math.sqrt(3)/4}")
elif b=="R2":
    a=float(input("R2 ni kiriting: "))
    print(f"Teng tomonli uchburchakning ichki chizilgan aylana radiusi{a/2}")
    print(f"Teng tomonli uchburchakning tashqi chizilgan aylana radiusi{a}")
    print(f"Teng tomonli uchburchakning yuzi {(6*(a/2)/math.sqrt(3))*math.sqrt(3)/4}")
elif b=="S":
    a=float(input("S ni kiriting: "))
    print(f"Teng tomonli uchburchakning ichki chizilgan aylana radiusi{(a*4/math.sqrt(3))*math.sqrt(3)/6}")
    print(f"Teng tomonli uchburchakning tashqi chizilgan aylana radiusi{(a*4/math.sqrt(3))*math.sqrt(3)/6*2} ")
    print(f"Teng tomonli uchburchakning yuzi {s}")
else:
    print(0)