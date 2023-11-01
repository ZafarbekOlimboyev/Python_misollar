"""
 n natural soni berilgan. Dastlabki n ta toq sondan tashkil topgan massivni hosil qiling va elementlarini chiqaring.
"""
import math

a=int(input("N ni kiriting:"))
b=[]
for i in range(1,2*a):
    if i%2==1:
        b.append(i)
print(b)