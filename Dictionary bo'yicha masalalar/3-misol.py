"""
Lug'atda berilgan kalit mavjudligini tekshirish uchun dastur
tuzing
"""
data={
    "apple":"olma",
    "bye":"hayr",
    "home":"uy"
}
n=input("Keyni kiriting: ")
print(data.setdefault(n))