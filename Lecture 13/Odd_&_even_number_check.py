# 12.7 even or odd check
def ev(num):
    if num%2==0:
        return True
    else:
        return False


Num=int(input("Input a Number: "))
n=ev(Num)
print(n)
