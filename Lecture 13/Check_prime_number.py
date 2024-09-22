# 12.10 Check Prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


pnumber = int(input("Input a Number: "))
print(f" {is_prime(pnumber)}! Is {pnumber} a prime number.")
