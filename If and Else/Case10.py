""" Robot faqat to'rtta tomonga ko'cha oladi('s"-shimol, "j" -Janub, "q"-sharq, "g"-g'arb) va uchta raqamli kamanda 0-harakni davom ettir,
 1-chapga bunl, 2-o'ngga bunl. Y robot yo'nalishi va K- kamanda berilgan. Berilgan kamanda bajarilgandan keying robot holatini aniqlovchi programma tuzilsin"""
a=int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
if a==1:
    b=input("Kamandani kiriting: ")
    if b=="s":
        print("Robot shimol tomonga burildi.")
    elif b=="j":
        print("Robot janub tomonga burildi.")
    elif b=="q":
        print("Robot sharq tomonga burildi.")
    elif b=="g":
        print("Robot G`arb tomonga burildi.")
    else:
        print(0)
elif a==0:
    c=int(input("Kamandani kiriting: "))
    if c==0:
        print("Robot harakatni davom ettirdi.")
    elif c==1:
        print("Robot chapga burildi.")
    elif c==2:
        print("Robot o`ngga burildi.")
    else:
        print(0)
else:
    print(0)