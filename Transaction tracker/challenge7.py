#this is a list that stores every transaction as indicated and each transaction in the list is a tuple
transactions = [
    (1,"john", 500, "successful"),
    (2,"mary", 200, "failed"),
    (3,"david", 900, "successful"),
    (4,"grace", 700, "successful"),
    (5,"Ethen", 100, "failed"),
    (6,"kent", 550, "sucessful"),
    (7,"dexter" , 700, "failed"),
    (8,"harry", 700, "sucessful"),
    (9, "angela", 450, "sucessful"),
    (10,"peter", 500, "successful")
    ]


def separate_transactions():

    successful = []
    failed = []

#this pratically says gos through the tuple in the list one by one. grab a file  and look inside
    for transaction in transactions:

#this checks if the position[3] is equal to successful it so it throws it into the the successful list 
        if transaction[3] == "successful":
            successful.append(transaction)

#this checks if it meets the condition and if it doesnt it stores it in the failed list
        else:
            failed.append(transaction)

    print("\nTransaction successful: ")
    for item in successful:
        print(item)

    print("\nFailed transaction: ")
    for item in failed:
        print(item)

#this means that the machine should hand the list of successful trnsactionss out to the rest of the program to use later
    return successful

def calculate_totals(successful):
    total = 0

    for transaction in successful:
#this takes the money from the transaction, sums them up and store them in total
        total += transaction[2]

    average = total / len(successful)

    print("\nTotal Successful amount:", total)
    print("Average successful amount:", average)

def top_transaction (successful):

#this takes all the money in the transaction list and arranges them from largest to smallest. Normally python stores these from smallest to largest but that is changed using reverse=True
    sorted_transaction  = sorted(successful,
                                 key=lambda transaction: transaction [2],
                                 reverse=True)
    print("\nTop 3 transactions: ")

    for transaction in sorted_transaction[:3]:
        print(transaction)

def search_customer():

#this locates your transaction by inputing your name
    search = input("\nEnter your name: ")

 #this is false because we havent searched yet   
    found = False

    for transaction in transactions:

        if transaction[1].lower() == search.lower():

            print(transaction)
            found = True

    if not found:
        print("Customer not found")

successful_transactions = separate_transactions()
calculate_totals(successful_transactions)
top_transaction(successful_transactions)
search_customer()
        
