"""
Berilgan sonlarni barchasini yig’indisini qaytaruvchi funksiya tuzing. (*args dan
foydalaning, sum() funksiyasidan foydalanmang).
"""
def yigindi(sonlar):
    """Bu funksiya sonlarni barchasini yig’indisini hisoblovchi funksiya """
    s=0
    for son in sonlar:
        s=s+son
    return s
sonlar=tuple(map(int, input().split()))
print(yigindi(sonlar))
