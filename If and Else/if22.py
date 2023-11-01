""" OX va OY koordinata o'qlarida yotmaydigan nuqta berilgan Nuqta joylashgan koordinata choragi aniqlansin. """
x=float(input("X ni qiymatini kiriting: "))
y=float(input("Y ni qiymatini kiriting: "))
if x==0 or y==0:
    print("Nuqta kordinata o`qida yotadi.")
elif x>0 and y>o:
    print("Nuqta birinchi chorakda joylashgan.")
elif x<0 and y>0:
    print("Nuqta ikkinchi chorakda joylashgan.")
elif x<0 and y<0:
    print("Nuqta uchinchi chorakda joylashgan.")
else:
    print("Nuqta to`rtinchi chorakda joylashgan.")