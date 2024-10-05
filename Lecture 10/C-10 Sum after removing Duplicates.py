n= int(input("How many numbers do you want to enter?__ "))
numbers=[]

for i in range(n):
    b=int(input(f"Enter number {i+1}: "))
    numbers.append(b)


#remove
remove_duplicates=[]

for num1 in numbers:
    if num1 not in remove_duplicates:
        remove_duplicates.append(num1)

#sum and average

sum=0
for n in remove_duplicates:
    sum+=n
avg=sum/len(remove_duplicates)


print("List after removing duplicates:", remove_duplicates)
print(f"Sum: {sum} and Average: {avg:.2f}")
