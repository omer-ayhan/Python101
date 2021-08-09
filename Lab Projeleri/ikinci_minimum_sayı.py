lists  = dict()
scores = []
results = []

for _ in range(int(input("number of students: "))):
    name = input("Student name: ")
    score = float(input("Score: "))
    lists[score] = lists.get(score, name)
    scores.append(score)
    
scores.sort()
print(lists)
if len(scores)>1:
    scores.remove(min(scores))
    print(lists[min(scores)],min(scores))
else:
    print(lists[min(scores)],min(scores))