#obtaining Factorial of a number using recursion
n=int(input('Enter the number: '))
def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)
result= factorial(n)
print("The factorial of", n, "is",result)
