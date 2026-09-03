# Checking whether numbers are prime
def check_prime(num):
    if num <= 1:
        return False

    # Checking whether the number is divisible by any smaller number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

numbers = [3, 7, 12, 19, 25, 29]

for n in numbers:
    if check_prime(n):
        print(f"{n} is a prime number!")
    else:
        print(f"{n} is not a prime number.")