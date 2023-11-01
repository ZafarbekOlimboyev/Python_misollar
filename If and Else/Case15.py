"""
O'yin kartasi turlari berilgan 1-g'isht, 2-olma, 3-chillak, 4-qarg'a. 10 lik kartadan katta kartalar
quyidagi qiymatlari o'zlashtirgan 11-valet 12-dama, 13-qirol, 14-tuz ikkita butun son benigan N-karta
qiymat (6<=N<=14), M-karta turi(1<=4) kiritilganda karta nomlarini (masalan: "olti qarg'a") chiqarb
beruvchi programma tuzilsin.
"""
m=int(input("Karta turi: "))
n=int(input("Kartalar qiymati: "))
g="g`isht."
o="olma."
c="chillak."
q="qarg`a."
if m==1:
    if 6<=n<=14:
        if n==6:
            print("Olti "+g)
        elif n==7:
            print("Yetti "+g)
        elif n==8:
            print("Sakkiz "+g)
        elif n==9:
            print("To`qqiz "+g)
        elif n==10:
            print("O`n "+g)
        elif n==11:
            print("O`n bir Valent " +g)
        elif n==12:
            print("O`n ikki Dama "+g)
        elif n==13:
            print("O`n uch Qirol "+g)
        elif n==4:
            print("O`n to`rt Tuz" +g)
    else:
        print(0)
elif m==2:
    if 6<=n<=14:
        if n==6:
            print("Olti "+o)
        elif n==7:
            print("Yetti "+o)
        elif n==8:
            print("Sakkiz "+o)
        elif n==9:
            print("To`qqiz "+o)
        elif n==10:
            print("O`n "+o)
        elif n==11:
            print("O`n bir Valent " +o)
        elif n==12:
            print("O`n ikki Dama "+o)
        elif n==13:
            print("O`n uch Qirol "+o)
        elif n==4:
            print("O`n to`rt Tuz" +o)
    else:
        print(0)
elif m==3:
    if 6<=n<=14:
        if n==6:
            print("Olti "+c)
        elif n==7:
            print("Yetti "+c)
        elif n==8:
            print("Sakkiz "+c)
        elif n==9:
            print("To`qqiz "+c)
        elif n==10:
            print("O`n "+c)
        elif n==11:
            print("O`n bir Valent " +c)
        elif n==12:
            print("O`n ikki Dama "+c)
        elif n==13:
            print("O`n uch Qirol "+c)
        elif n==4:
            print("O`n to`rt Tuz" +c)
    else:
        print(0)
elif m==4:
    if 6<=n<=14:
        if n==6:
            print("Olti "+q)
        elif n==7:
            print("Yetti "+q)
        elif n==8:
            print("Sakkiz "+q)
        elif n==9:
            print("To`qqiz "+q)
        elif n==10:
            print("O`n "+q)
        elif n==11:
            print("O`n bir Valent " +q)
        elif n==12:
            print("O`n ikki Dama "+q)
        elif n==13:
            print("O`n uch Qirol "+q)
        elif n==4:
            print("O`n to`rt Tuz" +q)
    else:
        print(0)
else:
    print(0)
