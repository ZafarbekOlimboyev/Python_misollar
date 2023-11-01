"""Oy raqami berilgan. Shu oyda nechta kun borligini aniqlovchi programma tuzilsin. """

a=int(input("Oyni tartib raqamini kiriting: "))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("Bu oyda 31 kun bor.")
elif a==2:
    print("Bu oyda 28 kun bor.")
else:
    print("Bu oyda 30 kun bor.")