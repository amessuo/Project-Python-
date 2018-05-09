def fib(n):
    if n==0:
        return [0]
    if n==1:
        return [0,1]
    else:
        l=fib(n-1)
        l.append(l[-1]+l[-2])
        return l

print(fib(5))

