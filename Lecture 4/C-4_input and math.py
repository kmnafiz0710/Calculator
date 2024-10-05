print("task 4.1")
print("\n")
n1,n2=map(int, input("Enter two number for summation: "). split())
print(f"The summation of {n1} and {n2} is {n1+n2}")
print("\n")


print("task 4.2")
print("\n")

name=input("Enter your Name: ")
age=input("Enter your age: ")
color=input("Enter your favorite Color: ")
print(f"Thank you for sharing your information.\n your name is {name}, Your age is {age} and your favorite color is {color}.")
print("Thank you for sharing your information.\n your name is {},Your age is {} and your favorite color is {}". format(name,age,color))
print("\n")


print("task 4.3")
print("\n")

r= float(input("Input the radius of a circle: "))
c=3.14*r*r
print(" The area of the circle is ",c)
print("\n")


print("task 4.4")
print("\n")
print("To convert the temparature from Celsius to Fahrenheit")
Celsius= float(input("Input the Celsius temparature: "))
Fahrenheit = (Celsius * 9/5) + 32
print(f"{Celsius}°Celsius = {Fahrenheit}° Fahrenheit.")
print("\n")


print("task 4.5")
print("\n")
a,b= map(float, input("Enter two Numbers: ").split() )
addition=a+b
subtraction=a-b
multiplication=a*b
divition=a/b
modulus=a%b
exponent=a**b

print("The Summation of these number is ",addition)
print("The Subtraction of these number is ",subtraction)
print("The Multiplication of these number is ",multiplication)
print("The Divition of these number is ",divition)
print("The Modulus of these number is ",modulus)
print("The Exponent of these number is ",exponent)

print("\n")


print("task 4.6")
print("\n")

age= int( input("Enter your age: "))
citizenship= input("Are you a citizen of Bangladesh? Type \"Yes\" or \"No\" ")
if age >= 18 and citizenship == Yes:
    print("You are a voter")
else:
    print("You are not a voter")

