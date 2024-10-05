print("Calculation and Printing way")

print("\n")

num_1=50
num_2=25
sum=num_1+num_2
print("The summation is:",sum)
subtract=num_1-num_2
print("The subtract is:",subtract)
multiply=num_1*num_2
print("The multiplication is:",multiply)
quotient=num_1/num_2
print("The quotient is:",quotient)
print("\n")

#another way for print
print("The summation of {} and {} is: {}". format(num_1,num_2,sum))
print("The subtract of {} and {} is: {}". format(num_1,num_2,subtract))
print("The multiplication of {} and {} is: {}". format(num_1,num_2,multiply))
print("The quotient of {} and {} is: {}". format(num_1,num_2,quotient))
print("\n")

#another way for print
print(f"The summation of {num_1} and {num_2} is: {sum}")
print(f"The subtract of {num_1} and {num_2} is: {subtract}")
print(f"The multiplication of {num_1} and {num_2} is: {multiply}")
print(f"The quotient of {num_1} and {num_2} is: {quotient}")

print("\n")
print("\n")

#kono word er pashe " " print korte chaile...
#extra sei quotetion(") er age (\) back slash use korte hobe.
print("May name is \"Khaled Masud\"")


#Get user input
number1= input("The first number is: ")
number1=int(number1)
number2= int( input("The second number is: "))
sum1=number1+number2

print(f"The summation of {number1} and {number2} is: {sum1}")

print("\n")
print("\n")
print("\n")
print("\n")


#Get multiple user input in one line.

num1,num2=map(int, input("Enter two numbers ").split())
summm=num1+num2
print(" The summation of this number is ", summm)


print("\n")
#num1=int( input("Enter your first number: "))
#num2=int( input("Enter your second number: "))
#num3=int( input("Enter your third number: "))

num1,num2,num3=map(int,input("enter three numbers: ").split())

sum=num1+num2+num3

print(f"The summation of {num1},{num2},{num3} is {sum} ")


