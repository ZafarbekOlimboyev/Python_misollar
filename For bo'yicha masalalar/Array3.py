"""
 n natural soni va arifmetik progressiyaning dastlabki hadi A va ayirmadi D berilgan.
Arifmetik progressiyaning dastlabki n ta hadidan tashkil topgan massivni hosil qiling va elementlarini chiqaring. A₁ =A+D
"""
n=int(input("Dastlabki hadlar sonini kiriting: "))
a=float(input("A1 ya`ni arifmetik progressiyaning 1-hadini kiriting: "))
d=float(input("D yani ayirmasini kiriting: "))
s=[]
for i in range(0,n):
    s.append("  a1=")
    s.append(a)
    a=a+d
print(*s)