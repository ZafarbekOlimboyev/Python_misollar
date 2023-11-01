"""
Uchta opa-singil TATU da o‘qishadi. Ular yangi yilga viloyatga o‘z uylariga qaytishdan oldin onalari uchun sovg‘a olishmoqchi.
Ular olmoqchi bo‘lgan sovg‘aning narxi NN so‘m. Yo‘l xarajatlaridan tashqari opa-singillarning to‘ng‘ichida AA so‘m, o‘rtanchasida
BB so‘m va kichigida CC so‘m ortiqcha pul bor. Ular onalari uchun olmoqchi bo‘lgan sovg‘ani ola olishadimi yoki yo‘qligini aniqlang.

Chiquvchi ma'lumotlar:
Opa - singillar onalariga sovg‘ani ola olishsa “Yes” aks holda “No” so‘zini chiqaring.
input:120000
      70000 40000 20000
output: Yes
"""
n=int(input())
a,b,c=map(int,input().split())
if a+b+c>=n:
  print("Yes")
else:
  print("No")