scores=list(map(int, input("Enter the score list: ").split()))
print(f"Original Scores: ",scores)
max_score=0

for s in scores:
    if s>max_score:
        max_score=s
print("Maximun score: ",max_score)

avg=100/max_score
# increased_score=avg*scores[s]

for i in range(len(scores)):
    scores[i]=scores[i] *avg


for i in range(len(scores)):
    if scores[i]<60:
        scores[i]=60

print(f"Final Scores: {scores}")
