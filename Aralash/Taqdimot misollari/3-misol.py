n=int(input())
b=[]
for i in range(1,n+1):
    if i%3==0 and i%5!=0:
        b.append('Fizz')
    elif i%5==0 and i%3!=0:
        b.append('Buzz')
    elif i%3==0 and i%5==0:
        b.append(f'FizzBuzz')
    else:
        b.append(f'{i}')
print(b)