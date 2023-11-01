"""
N soni berilgan, 1 dan N gacha bo’lgan sonlar ko’paytmasini rekursiv
funksiya yordamida hisoblaydigan dastur tuzing.
"""
def kopaytma(son):
    """Bu funksiya 1 dan N gacha bo’lgan sonlar ko’paytmasini hisoblaydi."""
    if son==1:
        return 1
    else:
        return son*kopaytma(son-1)
son=int(input("N ni kiriting: "))
print(kopaytma(son))