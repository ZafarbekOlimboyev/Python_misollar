"""
Paskal uchburchagining birinchi n qatorini chop etuvchi Python
funksiyasini yozing.
"""
import math
def Paskal_uchburchagi(n):
    """Bu funksiya Paskal uchburchagini dastlabki N-qatorini chiqarib beradi."""
    for qator in range(n+1):
        s=1
        qator_qiymatlari=[]
        for qatorlar in range(qator +1):
            h=math.factorial(qator)/(math.factorial(qatorlar)*math.factorial(qator-qatorlar))
            qator_qiymatlari.append(int(h))
            h=0
        print(qator_qiymatlari)
        qator_qiymatlari.clear()

n=int(input("N ni kiriting: "))
Paskal_uchburchagi(n)