"""
n! ni hisoblaydigan funksiya dasturini tuzing (Recursion function
ko’rinishida)
"""
def fact(son):
    """Bu funksiya faktaryalni hisoblaydi"""
    if son == 1:
        return 1
    else:
        return son * fact(son - 1)
son=int(input("N ni kiriting: "))
print(fact(son))