""" Koordinata o'qlariga parallel ravishda to'g'ri to'rtburchakning uchta uchi berilgan, to'rtinchi uchi koordinatasini aniqlansin."""
x1=float(input("X1 ni kiriting: "))
y1=float(input("Y1 ni kiriting: "))
x2=float(input("X2 ni kiriting: "))
y2=float(input("Y2 ni kiriting: "))
x3=float(input("X3 ni kiriting: "))
y3=float(input("Y3 ni kiriting: "))

if x1==x2 and y1==y3:
    print(f"To`rtinchi nuqta koordinatalar quyidagicha ({x3} ; {y2})")
elif x1==x2 and y2==y3:
    print(f"To`rtinchi nuqta koordinatalar quyidagicha ({x3} ; {y1})")
elif x2==x3 and y1==y2:
    print(f"To`rtinchi nuqta koordinatalar quyidagicha ({x1} ; {y3})")
else:
    print("Siz kiritgan ma`lumotlar to`gri emas.")