#write a python program that takes a single argument and check if yhe number is a paramreter or not 

def is_prime(n):
    if n < 2:
        return false 
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
if is_prime(num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')