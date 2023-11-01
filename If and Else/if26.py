""" X haqiqiy soni berilgan. Quyidagi funksiya hisoblansin.
       -x, agar x=<0;
F(x) = x^2, agar 0<x<2
       4, agar x>=2 """
x=float(input("X ni kiriting: "))
if x<=0:
    print(f" Javob: {-x}")
elif 0<x<2:
    print(f"Javob {x**2}")
else:
    print(4)