# Recursion is a function which call itself
# IT is used to directly use a mathematical formula as a function
# NOTE factorial(n)= n x factorial(n-1)

# n! = 1 * 2 * 3 * 4 .....*n
# NOTE n! = (n-1) * n

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return factorial_recursive(n-1)*n
#f = factorial_iter(5)
f = factorial_recursive(5)
print(f)