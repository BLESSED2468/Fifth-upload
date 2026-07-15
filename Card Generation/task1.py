first_name = input("Enter your name").strip()
last_name = input("Enter your last name").strip()
birth_year = input("what year where u born").strip()

first_part = first_name[:2]
second_part = last_name[-2:]
third_part = birth_year[-2:]

Id = (first_part + second_part +third_part).upper()

print("student ID", Id)