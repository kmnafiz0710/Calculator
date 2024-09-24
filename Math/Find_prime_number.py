def prime_finder(number):
    if number<=1:
        return False
    else:
        for n in range(2,int(number**0.5)+1):
            if number%n==0:
                return False
                break
        return True

number = int(input("Enter a number: "))


if prime_finder(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
