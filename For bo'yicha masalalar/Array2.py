"""
n natural soni berilgan. 2 sonining dastlabki n ta darajasidan tashkil topgan massivni hosil
qiling va elementlarini chiqaring. (1,2,4,8,...)
"""
a=int(input("N ni kiriting: "))
b=[]
for i in range(0,a):
    b.append(2**i)
print(b)