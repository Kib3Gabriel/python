#Write a recursive function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n* factorial(n-1)


print('Enter the number')
y = int(input())

result = factorial(y)
print(result)