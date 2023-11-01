# a va b o’zgaruvchisini e’lon qiling. A ning qiymatini b ga, b ni qiymatini a ga o’zgartiradigan kod yozing. (qo’shimcha o’zgaruvchi ishlatmang)
a=float(input("A sonini kiriting: "))
b=float(input("B sonini kiriting: "))
a, b = b, a
print(a,b)