"""
Standart kirituvchi ma’lumot sifatida ismlarni o’qib olib, ularning ichidan
eng uzunini chiqaruvchi dastur tuzing
"""
def uzunlik(ismlar):
    """Bu funksiya eng uzun so'zni topish uchun ishlatiladi."""
    uzunliklar=[]
    for i in ismlar:
        uzunliklar.append(len(i))
    eng_katta_qiymat=ismlar[uzunliklar.index(max(uzunliklar))]
    return eng_katta_qiymat
ismlar=input("Sonlarni kiriting: ").split()
print(uzunlik(ismlar))