numbers =set(map(int, input("Enter numbers: ").split()))
# ev_numbers=set()
for n in list(numbers):
    if n%2==0:
        numbers.discard(n)
print(f"After removing even numbers: {numbers}")
