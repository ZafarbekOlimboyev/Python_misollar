"""
n natural soni berilgan. Dastlabki n ta Fibonachchi sonlaridan tashkil topgan massivni hosil qiling va
elementlarini chiqaring.
FO = 1; F1 = 1; F[k] =F[k-1]+F[k-2]; k=2, 3, 4, ...
#Bu joyda Fibonachchi sonlir bo`yicha sal xato malumot berilgan ekan men to`g`irlab qo`ydim. Fibonachchi sonlari F0=0 F1=1 F2=1 va h.k
"""
n=int(input("N ni kiriting: "))
if n==1 or n==2:
    print("F0 = 0 F1 = 1 F2 = 1")
else:
    s=[" F0 = 0"," F1 =",1," F2 =",1,"F3 = 2"]
    h = 2
    z = 1
    for i in range(2,n):
        y=h+z
        s.append(f" F{i+2} =")
        s.append(y)
        z=h
        h=y
    print(*s)
