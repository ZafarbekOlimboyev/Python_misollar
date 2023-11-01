"""1-7 gacha bo'lgan butun sonlar berilgan.Kintigan songa mos ravishda
hafta kunlarini so'zda ifodalovchi programma tuzilsin (1-Dushanba 2-Chorshanba, hk)"""
a=int(input("Sonni kiriting: "))
b="shanba"
if a==1:
    print("Du"+b)
elif a==2:
    print("Se"+b)
elif a==3:
    print("Chor"+b)
elif a==4:
    print("Pay"+b)
elif a==5:
    print("Juma.")
elif a==6:
    print("Shanba.")
elif a==7:
    print("Yak"+b)
else:
    print(0)