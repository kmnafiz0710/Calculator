def prime(numbers):
    for num in numbers:
        if num<=1:
            return False
        else:
            for n in range(2, (num**0.5)+1):
                if num%n==0:
                    return False
                break
            return True
