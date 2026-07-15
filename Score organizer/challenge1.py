
#This is an empty list that stores all the scores from the students
scores = []

#this for loop runs ten times as indicated. it is what makes it possible for the program to ask for your scores ten times
for i in range(10):
    score = int(input(f"Enter score {i+1}: "))
   
# after inputing the scores this stores it in the list 'scores' from above
    scores.append(score)

#this part is identify the highest, lowest and average of the all the student scores
highest = max(scores)
lowest = min(scores)
average = sum(scores) / len (scores)

#this empty list store the scores the meet the passed condition and store the ones that don't meet the pass condition in failed
passed = [x for x in scores if x>50]
failed = [x for x in scores if x<50]

"""passed = []
failed = []
for score in scores:
    if score>=50:
        passed.append(score)
    else:
        failed.append(score)"""

scores.sort()

print("\nHighest scores: ", highest)
print("Lowest score:", lowest)
print("Average score:", average)

print("\nPassed scores: ", passed)
print("Failed scores:", failed)

print("\n Scores:", scores)