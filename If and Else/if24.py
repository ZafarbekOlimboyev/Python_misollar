""".X haqiqiy soni berilgan. Quyidagi funksiya hisoblansin
      2-sin(x), agar x>0;
f(x)=
      x-6, agar x≤0; """
import math
x=float(input("X ni kiriting: "))
if x>0:
    print("Javob: ",(2-math.sin(x)))
elif x<=0:
    print("Javob: ",(x-6))
