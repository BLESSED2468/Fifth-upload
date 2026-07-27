username = input('Enter your name')
uppercase_username = username.upper()

first_four = username[:4]

contains_underscore = "_" in username

contains_number = any(char.isdigit() for char in username)

print("uppercase:", uppercase_username)
print("first 4 characters:", first_four)
print("contains_:", contains_underscore)
print("contains Number:", contains_number)