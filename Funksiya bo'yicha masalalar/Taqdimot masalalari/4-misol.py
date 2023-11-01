"""
Standart kirituvchi ma’lumot sifatida ismlarni o’qib olib, ularning ichidan
eng kaltasini chiqaruvchi dastur tuzing
"""
def uzunlik(ismlar):
    """Bu funksiya eng qisqa so'zni topadi."""
    uzunliklar=[]
    for i in ismlar:
        uzunliklar.append(len(i))
    eng_qisqa_qiymat=ismlar[uzunliklar.index(min(uzunliklar))]
    return eng_qisqa_qiymat
ismlar=input("Sonlarni kiriting: ").split()
print(uzunlik(ismlar))