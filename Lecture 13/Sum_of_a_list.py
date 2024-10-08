# 12.9 sum of all elements in the list
def sum_list(numbers):
    summ=0
    for n in numbers:
        summ+=n
    return summ


Num_list=list(map(int, input("Enter numbers that you wanna sum: ").split()))
sum=sum_list(Num_list)
print(f"The summation of all element of this list is: {sum}")

# Its Final result.