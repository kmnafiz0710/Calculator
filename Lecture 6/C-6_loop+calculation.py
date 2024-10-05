
#Loop
N=1
while N<=20:
    print("Khaled Masud,", end=' ') #For one line print
    N += 1

print("\n")


S= int(input("Enter start number "))
End_number = int(input("Enter end number "))
i=int(input("Enter increasing number "))   #condition ta variable hishebe use kora hoyese.
while S<=End_number:
    print(S)
    S+=i


a=1
b=10
while a<=b:
    print(a)
    a+=1


s=0
i=0
while i<=10:
    i =i+1
    s=s+i
print(s)

#work 1



#i theke n porjonto summation korar system

s=0
i=int(input("Enter start number "))
n=20
while i<=10:
    i+=1
    s=s+i
    print(s)


#work 2

s=0
i=int(input("Enter start number "))
n=int(input("Enter end number "))
while i<=n:
    i+=1
    s=s+i
    print(s)


#work 3

#i theke n porjonto multiplication korar system


s=1
i=int(input("Enter start number "))
n=int(input("Enter end number "))
while i<=n:
    i+=1
    s=s*i
print(f"The multiplication of {i} and {n} is {s}")



cities=['Dhaka','Khulna','barishal','Feni']
for city in cities:
    print(city)




age=[33,54,23,76,53,34,18,22,12,6,45,26,19,20,29,56]
i=0


for a in age:
    if a>18:
        i+=1

print(f"Number of persons having age more than 20 is: {i}")



age=[33,54,23,76,53,34,18,22,12,6,45,26,19,20,29,56]
child=0
teen=0
adult=0
senior=0

for a in age:
    if a>=0 and a<=12:
        child=child+1

print(f"Child {child}")


#odd and Even Number

number=[10,20,23,34,21,10,23]
for a in number:
    if a%2==1:
        print(f"Odd number {a}")
for a in number:
    if a%2==0:
        print(f"Even number {a}")
        break



#Check age group
print("\n")
age= int(input("Enter your age "))
if age>=0:

    if age>=0 and age<=12:
        print(f"Your age is {age},You are a child.")
    elif age>=13 and age<=19:
        print(f"Your age is {age},You are a teen.")
    elif age>=20 and age<=64:
        print(f"Your age is {age},You are an Adult.")
    else:
        print(f"Your age is {age},You are a senior.")
else:
    print("Age is invalid")
