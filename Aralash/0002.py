"""
Sonlar ustida amallarning eng muximlaridan biri bu - taqqoslashdir. Ushbu masalada sizga qo'yilgan talab, ikkita butun sonni taqqoslash kerak bo'ladi
input: 0 0  output: =
input: 34 43  output: <
input: -34 -43  output: >
"""
a,b=map(int,input().split())
if a==b:
  print("=")
elif a>b:
  print(">")
else:
  print("<")