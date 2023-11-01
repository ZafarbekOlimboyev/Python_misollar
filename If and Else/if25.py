"""X haqiqiy soni berilgan. Quyidagi funksiya hisoblansin

     2-x, agar x<-2 yoki x>2;
f(x)=
     -3*x aks holda"""
x=float(input("X ni kiriting: "))
if x<-2 or x>2:
    print(f"Javob: {2-x}")
else :
    print(f"Javob: {x*(-3)}")