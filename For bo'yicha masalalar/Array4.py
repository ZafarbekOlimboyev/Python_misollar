"""
n natural soni va geometrik progressiyaning dastlabki hadi A va maxraji D berilgan.
Geometrik progressiyaning dastlabki n ta hadidan tashkil topgan massivni hosil qiling va elementlarini chiqaring. A₁ =AD
"""
n=int(input("Dastlabki hadlar sonini kiriting: "))
b=float(input("B1 ya`ni geometrik progressiyaning 1-hadini kiriting: "))
q=float(input("Q ni kiriting: "))
x=[]
for i in range(0,n):
    x.append("  B1=")
    x.append(b)
    b=b*q
print(*x)
