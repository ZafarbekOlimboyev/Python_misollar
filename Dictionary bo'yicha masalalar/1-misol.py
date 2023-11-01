"""
N butun soni berilgan. Ushbu misol yordamida dictionry yaratin:g
Example:
N = 1 => {0:10, 1:20},
N = 2 => {0:10, 1:20, 2:30}
"""
n=int(input())
x={}
for i in range(n+1):
    x[i]=(i+1)*10
print(x)