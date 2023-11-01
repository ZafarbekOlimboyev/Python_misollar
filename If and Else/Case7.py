"""Og'inik birliklari quyidagi tartibda berilgan 1-kilogramm, 2-milligramm, 3-gramm, 4-tonna, 5- sentner. Og'irlik birligini
 bildiruvchi soni berilgan va shu birlikdagi og'irlik qiymati berilgan. Og'irlikni kilogramda ifodalofchi programma tuzilsin."""
a=int(input("Og`irlikni bildiruchi sonni kiriting: "))
b=float(input("Og`irlik qiymatini kiriting: "))

if a==1:
    print(f" {b} kg ga teng.")
elif a==2:
    print(f"{b/1000000} kg ga teng.")
elif a==3:
    print(f"{b/1000} kg ga teng.")
elif a==4:
    print(f"{b*1000} kg ga teng.")
elif a==5:
    print(f"{b*100} kg ga teng.")
else:
    print(0)