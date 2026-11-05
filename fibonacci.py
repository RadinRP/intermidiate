def fibonatcci (n):
    if n <= 1 :
        return(n)
    return fibonatcci(n-1) + fibonatcci(n-2)
print(fibonatcci(8))