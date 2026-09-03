# Calculating the factorial of a number
def calculate_factorial(n):#1
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)#24

def display_result(number):
    print("The factorial of", number, "is:", calculate_factorial(number))

# Taking a number as input
num = int(input("Enter a number: "))
display_result(num)
