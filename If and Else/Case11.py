"""
 Lokatr dunyoning bir tomoniga qaratilgan('s-shimol, j-janub, q-sharq, g-g'arb) va uchta
raqamli kamanda: 0-o'ngga buril, 1-chapga buril, 2-burlish 180° C - lakatning boshlang'ich holat va K1, K2
kamandalar berilgan. Berilgan kamanda bajarilgandan keying lakatr holatini aniqlovchi programma tuzilsin.
"""
"""if 1==1:
    b=input("Lokatrning boshlang`ich holatini kiriting:")
    if b=="j":
        c=int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
        if c==1:
            k1=input("K1 ya`ni 1-buyruqni kiriting: ")
            if k1=="j":
                d=int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d==1:
                    k2=input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2=="j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2=="s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2=="q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2=="g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d==0:
                    k2 = int(input("K2 ya`ni 2-buyruqni kiriting: "))
                    if k2==1:
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2==0:
                        print("Lokatr G`arb tomonga qaragan.")
                    elif k2==2:
                        print("Lokatr Shimol tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0)

            elif k1=="s":
                d = int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d == 1:
                    k2 = input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2 == "j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == "s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == "q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == "g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d==0:
                    k2 = int(input("K2 ya`ni 2-buyruqni kiriting: "))
                    if k2==1:
                        print("Lokatr G`rab tomonga qaragan.")
                    elif k2==0:
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2==2:
                        print("Lokatr Janub tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0)

            elif k1=="q":
                d = int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d == 1:
                    k2 = input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2 == "j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == "s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == "q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == "g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d==0:
                    k2 = int(input("K2 ya`ni 2-buyruqni kiriting: "))
                    if k2==1:
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2==0:
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2==2:
                        print("Lokatr G'arb tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0)

            elif k1=="g":
                d = int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d == 1:
                    k2 = input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2 == "j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == "s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == "q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == "g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d==0:
                    k2 = int(input("K2 ya`ni 2-buyruqni kiriting: "))
                    if k2==1:
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2==0:
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2==2:
                        print("Lokatr sharq tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0)
            else:
                print(0)
        elif c==0:
            k1 = int(input("K1 ya`ni 1-buyruqni kiriting: "))
            if k1 == 0:
                d = int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d == 1:
                    k2 = input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2 == "j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == "s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == "q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == "g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d==0:
                    k2 = int(input("K2 ya`ni 2-buyurqni kiriting: "))
                    if k2==1:
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == 0:
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == 2:
                        print("Lokatr sharq tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0)
    elif b=="s":
        c = int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
        if c == 1:
            k1 = input("K1 ya`ni 1-buyruqni kiriting: ")
            if k1 == "j":
                d = int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d == 1:
                    k2 = input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2 == "j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == "s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == "q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == "g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d == 0:
                    k2 = int(input("K2 ya`ni 2-buyruqni kiriting: "))
                    if k2 == 1:
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == 0:
                        print("Lokatr G`arb tomonga qaragan.")
                    elif k2 == 2:
                        print("Lokatr Shimol tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0)

            elif k1 == "s":
                d = int(
                    input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d == 1:
                    k2 = input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2 == "j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == "s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == "q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == "g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d == 0:
                    k2 = int(input("K2 ya`ni 2-buyruqni kiriting: "))
                    if k2 == 1:
                        print("Lokatr G`rab tomonga qaragan.")
                    elif k2 == 0:
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == 2:
                        print("Lokatr Janub tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0)

            elif k1 == "q":
                d = int(
                    input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d == 1:
                    k2 = input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2 == "j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == "s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == "q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == "g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d == 0:
                    k2 = int(input("K2 ya`ni 2-buyruqni kiriting: "))
                    if k2 == 1:
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == 0:
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == 2:
                        print("Lokatr G'arb tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0)

            elif k1 == "g":
                d = int(
                    input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d == 1:
                    k2 = input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2 == "j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == "s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == "q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == "g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d == 0:
                    k2 = int(input("K2 ya`ni 2-buyruqni kiriting: "))
                    if k2 == 1:
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == 0:
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == 2:
                        print("Lokatr sharq tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0)
            else:
                print(0)
        elif c == 0:
            k1 = int(input("K1 ya`ni 1-buyruqni kiriting: "))
            if k1 == 0:
                d = int(input("Qanday kamanda bermoqchisiz harflimi yoki raqamli(Agar harfli bo`lsa 1 ni, aks holda 0): "))
                if d == 1:
                    k2 = input("K2 ya`ni 2-buyruqni kiriting: ")
                    if k2 == "j":
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == "s":
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == "q":
                        print("Lokatr Sharq tomonga qaragan.")
                    elif k2 == "g":
                        print("Lokatr G`arb tomonga qaragan.")
                    else:
                        print(0)
                elif d == 0:
                    k2 = int(input("K2 ya`ni 2-buyurqni kiriting: "))
                    if k2 == 1:
                        print("Lokatr Shimol tomonga qaragan.")
                    elif k2 == 0:
                        print("Lokatr Janub tomonga qaragan.")
                    elif k2 == 2:
                        print("Lokatr G'arb tomonga qaragan.")
                    else:
                        print(0)
                else:
                    print(0) 
     Ustoz 290 qatoryozganim bekor ketti. Men masala shartini xato tushunibman. """


a=input("Lokatr xolatini kiriting: ")
if a=="s":
    k1=int(input("K1 buyruqni kiriting (0/1/2): "))
    k2=int(input("K2 buyruqni kiriting (0/1/2): "))
    if k1==0 and k2==0:
        print("Lokatr Janub tomonga qaragan.")
    elif k1==0 and k2==1:
        print("Lokatr Shimol tomonga qaragan.")
    elif k1==0 and k2==2:
        print("Lokatr G`arb tomonga qaragan.")
    elif k1==1 and k2==0:
        print("Lokatr Shimol tomonga qaragan.")
    elif k1==1 and k2==1:
        print("Lokatr Janub tomonga qaragan.")
    elif k1==1 and k2==2:
        print("Lokatr Sharq tomonga qaragan.")
    elif k1==2 and k2==0:
        print("Lokatr G`arb tomonga qaragan.")
    elif k1==2 and k2==1:
        print("Lokatr Sharq tomonga qaragan.")
    elif k1==2 and k2==2:
        print("Lokatr Shimol tomonga qaragan.")
elif a=="j":
    k1 = int(input("K1 buyruqni kiriting (0/1/2): "))
    k2 = int(input("K2 buyruqni kiriting (0/1/2): "))
    if k1 == 0 and k2 == 0:
        print("Lokatr Shimol tomonga qaragan.")
    elif k1 == 0 and k2 == 1:
        print("Lokatr Janb tomonga qaragan.")
    elif k1 == 0 and k2 == 2:
        print("Lokatr Sharq tomonga qaragan.")
    elif k1 == 1 and k2 == 0:
        print("Lokatr Janub tomonga qaragan.")
    elif k1 == 1 and k2 == 1:
        print("Lokatr Shimol tomonga qaragan.")
    elif k1 == 1 and k2 == 2:
        print("Lokatr G`arb tomonga qaragan.")
    elif k1 == 2 and k2 == 0:
        print("Lokatr Sharq tomonga qaragan.")
    elif k1 == 2 and k2 == 1:
        print("Lokatr G`rab tomonga qaragan.")
    elif k1 == 2 and k2 == 2:
        print("Lokatr Janb tomonga qaragan.")
elif a=="q":
    k1 = int(input("K1 buyruqni kiriting (0/1/2): "))
    k2 = int(input("K2 buyruqni kiriting (0/1/2): "))
    if k1 == 0 and k2 == 0:
        print("Lokatr G`arb tomonga qaragan.")
    elif k1 == 0 and k2 == 1:
        print("Lokatr Sharq tomonga qaragan.")
    elif k1 == 0 and k2 == 2:
        print("Lokatr Shimol tomonga qaragan.")
    elif k1 == 1 and k2 == 0:
        print("Lokatr Sharq tomonga qaragan.")
    elif k1 == 1 and k2 == 1:
        print("Lokatr G`arb tomonga qaragan.")
    elif k1 == 1 and k2 == 2:
        print("Lokatr Janub tomonga qaragan.")
    elif k1 == 2 and k2 == 0:
        print("Lokatr Shimol tomonga qaragan.")
    elif k1 == 2 and k2 == 1:
        print("Lokatr janub tomonga qaragan.")
    elif k1 == 2 and k2 == 2:
        print("Lokatr Sharq tomonga qaragan.")
    else:
        print(0)
elif a=="g":
    k1 = int(input("K1 buyruqni kiriting (0/1/2): "))
    k2 = int(input("K2 buyruqni kiriting (0/1/2): "))
    if k1 == 0 and k2 == 0:
        print("Lokatr Sharq tomonga qaragan.")
    elif k1 == 0 and k2 == 1:
        print("Lokatr G`arb tomonga qaragan.")
    elif k1 == 0 and k2 == 2:
        print("Lokatr Janub tomonga qaragan.")
    elif k1 == 1 and k2 == 0:
        print("Lokatr G`arb tomonga qaragan.")
    elif k1 == 1 and k2 == 1:
        print("Lokatr Sharq tomonga qaragan.")
    elif k1 == 1 and k2 == 2:
        print("Lokatr Shimol tomonga qaragan.")
    elif k1 == 2 and k2 == 0:
        print("Lokatr Janub tomonga qaragan.")
    elif k1 == 2 and k2 == 1:
        print("Lokatr Shimol tomonga qaragan.")
    elif k1 == 2 and k2 == 2:
        print("Lokatr G`arb tomonga qaragan.")
    else:
        print(0)