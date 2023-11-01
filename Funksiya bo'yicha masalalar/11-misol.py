"""
Berilgan matn Palindrom ekanligini tekshiruvchi dastur tuzing.
"""
def palindrom(word):
    """Bu funksiya so`zni palindrom yoki palindrom emasligini aniqlaydi."""
    son=0
    last_index=len(word)-1
    for tekshirish in range(len(word)//2):
        if word[tekshirish] == word[last_index]:
            son=0
        else:
            son=100
        if son==100:
            return "Palindrom so'z emas."
        else:
            return "Palindrom so'z."

word=input("So'zni kiriting: ").lower()
print(palindrom(word))