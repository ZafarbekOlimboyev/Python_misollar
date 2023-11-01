"""
Beshta musbat butun son berilgan, ulardan to'rttasini ajratib olinganda umumiy yig'indisi bo'lishi mumkin bo'lgan minimum qiymat va maksimum qiymatni aniqlang
input: 1 2 3 4 5  output:10 14
"""
a,b,c,d,e=map(int,input().split())
print(a+b+c+d+e-max(a,b,c,d,e), a+b+c+d+e-min(a,b,c,d,e))