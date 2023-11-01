"""
Berilgan sonlar ichidan eng kattasini topuvchi funksiya tuzing.(Eslatma min(), max()
funksiyalaridan foydalanmang.
"""
def eng_katta_son(sonlar):
    """Bu funksiya sonlar ichidan eng katta sonni qaytaradi."""
    katta = sonlar[0]
    for son in sonlar:
        if katta>son:
            katta = katta
        else:
            katta = son
    return katta
sonlar=list(map(int,input().split()))
print(eng_katta_son(sonlar))