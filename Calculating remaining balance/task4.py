airtime_balance = float(input("Enter your airtime balance"))
amount = float(input("Enter the amount you want to share "))
fee= float(input("Enter the transfer fee for the amount shared"))

remaining_balance = airtime_balance - amount - fee
minimum_balance = remaining_balance >=100

print(remaining_balance)
print("Has minimum balance: " , minimum_balance)
