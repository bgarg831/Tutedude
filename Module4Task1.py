def factorial(a):
    if a<2:
        return 1
    else:
        return a * (factorial(a-1))


n=int(input('Enter a number: '))
m = factorial(n)
print('Factorial of n is:',m)


