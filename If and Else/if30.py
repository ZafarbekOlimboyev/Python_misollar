""" 1-999 oraliqdagi sonlar berilgan. Berilgan sonni "ikki xonali juft son", "uch xonali toq son
 va xk ekranga yozadigan programma tuzilsin."""
a=int(input("Sonni kiriting: "))
if 1<=a<=999:
    if 1<=a<=9:
        if a%2==1:
            print("Bir xonali toq son.")
        else:
            print("Bir xonali just son.")
    elif 10<=a<=99:
        if a%2==1:
            print("Ikki xonali toq son.")
        else:
            print("Ikki xonali juft son")
    else:
        if a%2==1:
            print("Uch honali toq son.")
        else:
            print("Uch honali juft son.")