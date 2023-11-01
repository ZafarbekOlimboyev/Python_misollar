"""Butun son berilgan. Berilgan sonni "musbat toq son", "mantly juft son", "son nolga teng" va x.k."""
a=int(input("Sonni kiriting: "))
if a>0 and a%2==1:
    print("Berilgan son musbat toq son.")
elif a>0 and a%2==0:
    print("Berilgan son musbat juft son.")
elif a==0:
    print("Berilgan son 0 ga teng.")
elif a<0 and a%2==1:
    print("Berilgan son manfiy toq son.")
else:
    print("Berilgan son manfiy just son.")