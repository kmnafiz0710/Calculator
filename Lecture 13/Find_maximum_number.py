# 12.6 Find maximum numbers
def max_number(numbers):
    max_n=0
    for n in numbers:
        if n>max_n:
            max_n=n
    return max_n


Number_list=list(map(int, input("Enter numbers: ").split()))
Maximum_number=max_number(Number_list)
print(f"The maximum numbers of this list is: {Maximum_number}")
