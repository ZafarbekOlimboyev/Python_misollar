"""
Parametr sifatida matnli ma’lumot qiluvchi funksiya yarating. Bunda
berilgan matnda nechta katta xarf, nechta kichik xarf, nechta raqam
bor ekanigini qaytarsin.
"""
def aniqlovchi(*matn):
    """Bu funksiya matnda nechta katta xarf, nechta kichik xarf, nechta raqam bor ekanigini aniqlaydi."""
    katta_harf=0
    kichik_harf=0
    raqam=0
    for word in matn:
        for harf in word:
            if harf == harf.upper() and harf!="." and harf!='0' and harf!='1'and harf!='2' and harf!='3'and harf!='4' and harf!='5'and harf!='6' and harf!='7'and harf!='8' and harf!='9':
                katta_harf += 1
            elif harf == harf.lower() and harf!="." and harf!='0' and harf!='1'and harf!='2' and harf!='3'and harf!='4' and harf!='5'and harf!='6' and harf!='7'and harf!='8' and harf!='9':
                kichik_harf += 1
            elif harf == ".":
                continue
            else:
                raqam +=1
    return f"Katta harflar {katta_harf}, kichik harflar {kichik_harf}, raqamlar {raqam}"
matn=tuple(input("Matnni kiriting: ").split())
print(aniqlovchi(*matn))