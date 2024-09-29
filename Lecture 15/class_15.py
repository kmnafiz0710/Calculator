def prime(num):
        if num<=1:
            return False
        else:
            for n in range(2, int(num**0.5)+1):
                if num%n==0:
                    return False
            return True

def prime_finder(numbers):
    primes=[]
    for n in numbers:
        if prime(n):
            primes.append(n)
    return primes


def digit_sum(number):
    s=0
    for n in number:
        s+=n
        return s



numbers=list(map(int, input("Enter numbers: ").split()))
# prime_Numbers=[]
prime_Numbers= prime_finder(numbers)
print("Prime numbers are: ",prime_Numbers)

Prime_Sum=sum(prime_Numbers)
print("Sum of all prime numbers: ",Prime_Sum)

ss= digit_sum(Prime_Sum)
print(f"Sum of {Prime_Sum}'s digit is {ss}")

