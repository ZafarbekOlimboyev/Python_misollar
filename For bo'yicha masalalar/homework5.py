"""
Standart kiruvchi ma'lumotdagi vergullar bilan ajratilgan so'zlar ketma-ketligi orasida maqsad qilingan so'z aynan qaysi indeksda turganligini aniqlovchi dastur tuzing
Ismlar: john, alice, bob
Maqsad: bob
Natija: 2
"""
ism=input().split(",")
maqsad=input()
print(ism.index(maqsad))
