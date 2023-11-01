"""
Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligida maqsad qilingan so'z necha marta takrorlanganligini aniqlovchi dastur tuzing Masalan:
Ismlar: alice, john, bob, alice, bob, john, alice
Maqsad: alice
Natija: 3
"""
ism=input().split(",")
maqsad=input()
print(ism.count(maqsad))