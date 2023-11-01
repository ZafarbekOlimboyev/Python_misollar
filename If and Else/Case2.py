"""K butun soni berilgan Baho natijalarini chiqaruvchi programma tuzing(1-yomon, 2-qoniqarsiz, 3-qoniqarli, 4-yahshi, 5-a'lo).
 Agar k soni 1-5 gacha oraliqqa tegishil bo'lmasa "xato" deb chiqarilsin"""
k=int(input("K sonini kiriting: "))
if k==1:
    print("Yomon.")
elif k==2:
    print("Qoniqarsiz.")
elif k==3:
    print("Qoniqarli.")
elif k==4:
    print("Yaxshi")
elif k==5:
    print("A`lo")
else:
    print("Xato")