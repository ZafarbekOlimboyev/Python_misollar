"""
Argument sifatida ismni o’qib olib, natija sifatida o’sha ismga salom
deydigan funktsiya tuzing.
"""
def salom(ism):
    """ Bu funksiya orqali foydalanuvchitomonidan kiritgan ismga  Salom beriladi."""
    print("Assalomu Aleykum", ism)
ism = input("Ism kiriting: ").title()
salom(ism)
