"""
Berilgan sonlar ichidan eng kichigini topuvchi funksiya tuzing.(Eslatma min(), max()
funksiyalaridan foydalanmang.
"""
def eng_kichik_son(sonlar):
    """Bu funksiya sonlar ichidan eng kichik sonni qaytaradi."""
    kichik = sonlar[0]
    for son in sonlar:
        if kichik<son:
            kichik = kichik
        else:
            kichik = son
    return kichik
sonlar=list(map(int,input().split()))
print(eng_kichik_son(sonlar))