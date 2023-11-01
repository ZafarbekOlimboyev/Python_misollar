"""
N ta elementdan iborat ro’yxat berilgan. Manashu ro’yxatda 1 dan
ortiq takrorlangan elementlarni faqat bittadan iborat ro’yxat
sifatida qaytaradigan funksiya dasturini tuzing.
"""
def dublikatlarni_tozalovchi(elementlar):
    """Bu funksiya berilgan ro'yxatdagi elementlar dublikatlarini o'chirib tashlash uchun ishlatiladi.Ya`ni ro'yxatdaa elementlarni
     1 dan ortiq nusxasi bo'lsa, 1 donasini qoldirib qolganlarinio'chirib tashlaydi."""
    for element in elementlar:
        elementlar_soni=elementlar.count(element)
        if elementlar_soni == 1:
            continue
        elif elementlar_soni >1:
            for tozalash in range(0,elementlar_soni-1):
                elementlar.remove(element)
    return elementlar

elementlar=input("Elementlarni kiriting: ").split()
print(dublikatlarni_tozalovchi(elementlar))