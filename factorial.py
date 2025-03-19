result = 1
n = int(input("Enter a number "))
for i in range(1, n+1):
    result *= i
print(f'Factorial of {n} is {result}')
