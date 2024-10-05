
# Count student award
print("\n")
print("count student who get award")
print("\n")

students=list(map(int, input("Enter all the score (Separate by space): ").split()))
Gold_medal=0
Silver_medal=0
Bronze_medal=0
Participation_award=0

for a in students:
    if a>90:
        Gold_medal+=1
    elif a>80 and a<=90:
        Silver_medal+=1
    elif a>70 and a<=80:
        Bronze_medal+=1
    elif a<70:
        Participation_award+=1


print(f"Gold Medal: {Gold_medal} Student")
print(f"Silver Medal: {Silver_medal} Student")
print(f"Bronze Medal: {Bronze_medal} Student")
print(f"Participation Award: {Participation_award} Student")

print("\n")

