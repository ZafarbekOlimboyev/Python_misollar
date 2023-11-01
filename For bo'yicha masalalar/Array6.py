"""
 n natural soni va A, B butun sonlari berilgan (n>2). a[0] = A; a[1] = B; boshqa elementlari o'zidan oldingi barcha
 elementlari yig'indisiga teng bo'lgan massivni hosil qiling va elementlarini chiqaring.

"""

n=int(input("N ni kiriting: "))
a,b=map(int,input("A va B ni kiritng: ").split())
s=[a,b]
h=a+b
for i in range(2,n):
    s.append(h)
    h*=2
print(*s)