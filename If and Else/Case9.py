""" Ikkita butun son berigan D (kun) va M (oy) (Kabisa bo`lmagan yil sanasi kintiladi) Berilgan
sanadan keyingi sanani ifodalovchi programma tuzilsin"""
d=int(input("Kunni kiriting: "))
m=int(input("Oyni kiriting: "))
if 1<=d<=30:
    print(f"keyingi sana. {m}-oyning {d+1}-kuni.")
elif d==31:
    if m==12:
        print("Keyingi sana. 1-oyning 1-kuni")
    else:
        print(f"Keyingi sana. {m + 1}-oyning 1-kuni")
else:
    print(0)