"""
n! ni hisoblaydigan funksiya dasturini tuzing (Recursion funcsiya
ko’rinishida emas)
"""
def fact(son):
    """Bu funksiya faktaryalni hisoblaydi"""
    s=1
    for i in range(1,son+1):
        s *=i
    return s
son=int(input("N ni kiriting: "))
print("Javob: ",fact(son))