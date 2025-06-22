# write a program to calculate factorial of a number
def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
num = int(input("Enter a number to calculate its factorial: "))
print(factorial(num))  # Output: 120

def getAge(age):
    return "your age is " + str(age)

print(getAge("20"))  # Output: your age is 20
print(getAge(20))  # Output: your age is 20