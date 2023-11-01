""". Yil berilgan (musbat butun son). Berilgan yilda nechta kun borligini aniqlovchi programma tuzilsin.
 Kabisa yilida 366 kun bor, kabisa bo'lmagan yilda 365 kun bor Kabisa yil deb 4 ga karrali yillarga aytiladi.
  Lekin 100 ga karrali yillar ichida faqat 400 ga karrali bo'lganlari kabisa yil hisoblanadi.
 Masalan 300, 1300 va 1900 kabisa yili emas. 1200 va 2000 kabisa yili."""
a=int(input("Yilni kiriting: "))
if (a%4==0 and a%100!=0) or a%400==0:
    print("Kasiba yili. Bu yilda 366kun bor.")
else:
    print("Kasiba yili emas. Bu yilda 365 kun bor.")