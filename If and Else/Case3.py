"""Oy raqamini benigan Kiritilgan oy qaysi fasiga tegishli ekanligini chiqaruvchi programma
tuzilsin. (Masalan 2 chi oy, "qish")"""
a=int(input("Raqamni kiriting: "))
if 3<=a<=5:
    if a==3:
        print("3-oy Bahor.")
    elif a==4:
        print("4-oy Bahor.")
    else:
        print("5-oy Bahor.")
elif 6<=a<=8:
    if a==6:
        print("6-oy Yoz.")
    elif a==7:
        print("7-oy Yoz.")
    else:
        print("8-oy Yoz.")
elif 9<=a<=11:
    if a==9:
        print("9-oy Kuz.")
    elif a==10:
        print("10-oy Kuz.")
    else:
        print("11-oy Kuz.")
elif a==12:
    print("12-oy Qish.")
elif a==1:
    print("1-oy Qish.")
elif a==2:
    print("2-oy Qish.")
else:
    print(0)