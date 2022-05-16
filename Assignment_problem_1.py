# for fibbonacci series from 0 to 50
a=0
b=1
print(a)
print(b)
for i in range(2,50):
    c=a+b
    a=b
    b=c
    # we need numbers less tham 50 only so this if is used
    if c<50:
     print(c)