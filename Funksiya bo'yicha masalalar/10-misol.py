"""
Ikkita butun x va y sonlari berilgan. Bunda x soni y soniga bo’linish
yoki bo’linmasligini aniqlovchi dastur tuzing.
"""
# Bu joyda adashmasam butun bo'lish nazarda tutilgan.
def butun_bolish(x,y):
    """Bu funksiya x sonini y soniga butun bo’linish yoki butun bo’linmasligini aniqlaydi."""
    if x/y-int(x/y)==0:
        return "Butun bo'lib bo'ladi."
    else:
        return "Butun bo`lib bo`lmaydi."
x=int(input("X ni kiriting: "))
y=int(input("Y ni kiriting: "))
print(butun_bolish(x,y))