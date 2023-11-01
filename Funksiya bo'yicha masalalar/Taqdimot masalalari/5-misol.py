"""
Parametr sifatida ismni o’qib olib, uni teskari tartibda chiqarib beradigan
funksiya tuzing.
"""
def teskari_tartib(ism):
    """Bu funksiya ismni o’qib olib, uni teskari tartibda chiqarib beradi."""
    ism=ism[-1::-1]
    return ism
ism=input("Ismni kiriting: ").title()
print(teskari_tartib(ism))