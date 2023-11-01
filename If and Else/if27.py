"""X haqiqiy soni berilgan. Quyidagi funksiya hisoblansin.
       0, agar x<0
F(x)=  1, agar xe[0,1),[2,3)
      -1, agar xe[1,2),[3,4)

"""
x=float(input("X ni kiriting: "))
if x<0:
    print(0)
elif (x%2==0)<=x<(x%2!=0):
    print(-2)
elif (x%2!=0)<=x<(x%2==0) :
    print(-1)