English = int(input("Enter your total  score in english "))
Math = int(input("Enter your total score in math "))
science = int(input("Enter your total score in science "))

total_score = English + Math + science

average_score = total_score / 3

print("="*10 , "RESULT SUMMARY" , "="*10)
print("Total score", total_score)
print("Average score", average_score)