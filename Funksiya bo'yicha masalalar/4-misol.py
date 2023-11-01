"""
Matn ko’rinishidagi ma’lumot berilgan. Shu mantni teskari tartibda chiqaruvchi
funksiya tuzing.
"""
def teskari_matn(matn):
    """Bu funksiya matnni hamda matn ichidagi so'zlarni ham teskari chiqarib beradi."""
    teskari=[]
    for word in matn:
        teskari.append(word[-1::-1])
    return teskari
matn=input("Matnni kiriting: ").split()
teskari_matn(matn).reverse()
matn.reverse()
print("Teskari matn hamda matn ichidagi so'zlar teskari chiqarilgan: ",*(teskari_matn(matn)))
print("Bu teskari matn :",*matn)
