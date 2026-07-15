full_name = input("Enter your full name ").strip()
num = str(input("Enter your favourite number "))

name = full_name.lower()

abrevated_name = name[:3]
 
user_name = (abrevated_name + num)

print(user_name)
