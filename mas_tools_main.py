from mas_tools import *
A = int(input("your first number"))
B = int(input("your secound number"))
C = str(input("what to do"))
if C == "+":
    print(plus(A , B))
elif C == "-":
    print(minues(A , B))
elif C == "/":
    print(dividing(A , B))
elif C == "*":
    print(multiplication(A , B))