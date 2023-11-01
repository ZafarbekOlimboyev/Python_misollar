"""
Tengyonli uchburchakning elementari quyidagi tartibda nomerlangan. 1-katet a, 2-gipotenuza c=√2, 3-gepotenuzaga tushirilgan baladik h=c/2, 4-yuzasi
s=(c*h)/2 . Shu elementlardan bittasi berilganda qolganlarini topuvchi programma tuzilsin.
"""
import math

b=input("Qaysi elementni kiritmoqchisiz (a/c/h/s) : ")
if b=="a":
    a=float(input("Katetni kiriting: "))
    print(f"Teng yonli uchburchakning yuzi {((a*math.sqrt(2))*(a*math.sqrt(2))/2)/2 } \nUchburchakning gipatenuzasi {a*math.sqrt(2)} \nGipatenuzaga tushurilgan balandlik {(a*math.sqrt(2))/2} \nUchburchak kateti {a}")
elif b=="c":
    a = float(input("Gipatenuzani kiriting: "))
    print(f"Teng yonli uchburchakning yuzi {a**2/2} \nUchburchakning gipatenuzasi {a} \nGipatenuzaga tushurilgan balandlik {a/ 2} \nUchburchak kateti {a/math.sqrt(2)}")
elif b=="h":
    a = float(input("Gipatenuzani kiriting: "))
    print(f"Teng yonli uchburchakning yuzi {a**2} \nUchburchakning gipatenuzasi {a*2} \nGipatenuzaga tushurilgan balandlik {h} \nUchburchak kateti {(2*h)/math.sqrt(2)}")
elif b=="s":
    a = float(input("Gipatenuzani kiriting: "))
    print(f"Teng yonli uchburchakning yuzi {a} \nUchburchakning gipatenuzasi {math.sqrt(4*a)} \nGipatenuzaga tushurilgan balandlik {math.sqrt(a)} \nUchburchak kateti {math.sqrt(4*a) / math.sqrt(2)}")
else:
    print(0)