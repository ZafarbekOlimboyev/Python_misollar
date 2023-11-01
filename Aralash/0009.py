"""
Sizga butun sonlar to'plami berilgan. To'plamda 1 ta elementdan tashqari barchasini jufti bor. To'plamdagi yagona jufti bo'lmagan yolg'iz sonni toping.
Masalan: [1,2,3,4,3,2,1][1,2,3,4,3,2,1] to'plamida yolg'iz son 44 sonidir.
input:1
      1
output:1
input: 3
       1 1 2
output: 2
input:5
      0 0 1 2 1
output:2
"""
a=int(input())
b=list(map(int,input().split()))
for c in b:
  if b.count(c)==1:
     print(c)