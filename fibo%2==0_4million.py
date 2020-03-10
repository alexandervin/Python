fib_seq = {}

#git def fib_iterative(n):
    if n in fib_seq.keys():
        return fib_seq[n]
    a,b,x = 0,1,n
    while x > 0:
        a,b = b,a + b
        x-=1
    fib_seq[n]=a
    return a

summ = 0
last_fib = i = 0
while last_fib <= 4000000:
    last_fib=fib_iterative(i)
    if last_fib % 2 ==0:
        summ+=last_fib
    i+=1

print(summ)
