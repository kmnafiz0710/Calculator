# 12.8 Factorial Check
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


number = int(input("Input a Number: "))
print(f"The factorial of {number} is {fact(number)}")
