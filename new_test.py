numbers=int(input("how many fib you want"))
fib1 = 1
fib2 = 2
for i in range (numbers):
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
print(fib3)