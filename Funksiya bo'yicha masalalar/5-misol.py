"""
range() funksiyasi bilan bir xil tartibda ishlaydigan clone_range() nomli funksiya
dasturini tuzing. Bunda default holatdagi qiymatlar uchun ham bir xil ishlasin.
"""
def clone_range(x=0,y=0,z=0):
    """Bu funksiya range funksiyasi bilan bir xil ishlaydi."""
    if y==0:
        son=0
    elif y!=0 and z==0:
        son = 1
    else:
        son = 2
    if son == 0:
        def clon_range(start=0,stop=x,step=1):
            sonlar = []
            while stop>start:
                sonlar.append(start)
                start +=step
            return sonlar
        return clon_range(0,x,1)
    elif son == 1:
        def clon_range(start=x,stop=y,step=1):
            sonlar = []
            while stop > start:
                sonlar.append(start)
                start += step
            return sonlar
        return clon_range(x,y,1)
    elif son == 2:

        def clon_range(start=x,stop=y,step=z):
            sonlar = []
            while stop > start:
                sonlar.append(start)
                start += step
            return sonlar
        return clon_range(x,y,z)
    else:
        return "Error"
for i in clone_range(2, 23,3):
    print(i)