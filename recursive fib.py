def fib(n):
    if (n <=1):
        return n
    else:
        return(fib(n-1) + fib(n-2))
nterms=int(input("entr a number"))
if(nterms<=0):
    print("enter a positive number")
else:
    for i in range(nterms):
        print(fib(i))

