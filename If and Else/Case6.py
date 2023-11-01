""" Uzinlik birliklari quyidagi tartibda berilgan 1-desimetr, 2-kilometr, 3-metr, 4-millimeter, 5-
santimetr. Uzunlik birligini bildiruvchi son berilgan (1 -- 5 oraliqda) va shu birlikdagi kesma uzunligi
berilgan (haqiqiy son) Kesmaning uzunligini metrlarda ifodalochi programma tuzilsin"""

a=int(input("Uzinlikni bildiruchi sonni kiriting: "))
b=float(input("Kesma uzunligini kiriting: "))

if a==1:
    print(f" {b/10} metr ga teng.")
elif a==2:
    print(f"{b*1000} metr.")
elif a==3:
    print(b,"metr.")
elif a==4:
    print(f"{b/1000} metr.")
elif a==5:
    print(f"{b/100} metr.")
else:
    print(0)