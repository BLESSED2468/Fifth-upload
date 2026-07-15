#this is a list that contains all the seat records which in this case are all tuples
seats = [
    ("A12", "David", "VIP"),
    ("B12", "Sarah", "Regular"),
    ("C12", "John", "VIP"),
    ("D12", "Mike", "Economy"),
    ("E12", "Grace", "Regular")

]

print("Seat Records: ")
#loops through every tuple in the list "seat"
for seat in seats:
    print(seat)

#the user searches for a search by inputing seat number
search = input("\n enter seat number to search: ")

#this is a boolean variable that tracks whether the seat inputted by the user was found
found = False

#this loops through all the tuple
for seat in seats:
#what happens here is tuple unpacking which separate the tuple values into variables
    seat_number, occupant, section = seat

#this checks if the seat in the tuple matches with the user input
    if seat_number == search:
        print("\n seat found: ")
        print("seat number: ", seat_number)
        print("occupant: ", occupant)
        print("section: ", section )
        
        found = True



if not found:
    print("seat not found")

section_count = {}

for seat in seats:
    section = seat[2]

    if section in section_count:
        section_count[section] += 1

    else:
        section_count[section] = 1

print("\n Section counts: ")
print(section_count)

