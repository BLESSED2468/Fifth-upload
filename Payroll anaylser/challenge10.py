employees = [
    {"name": "james", "department": "IT", "salary": 5500},
    {"name": "henry", "department": "HR", "salary": 4000},
    {"name": "nick", "department": "HR", "salary": 6000}
]

def salary_analysis():

    highest = max(employees, key = lambda employee: employee["salary"])

    lowest = min (employees, key = lambda employee: employee["salary"])

    print("\nhighest paid:", highest)
    print(highest)

    print("\nlowest paid:", lowest)
    print(lowest)

def average_salary():
    departments = {}
    for  employee in employees:
        dept = employee["department"]
        salary = employee["salary"]

        if dept not in departments:
            departments[dept] = []
        departments[dept].append(salary)

    print("\nAverage salary per department: ")

    for dept in departments:
        average = sum(departments[dept]) / len(departments[dept])
        print(dept, ":", average)

def search_department ():

    search = input("\nenter department: ")
    
    found = False

    for employee in employees:

        if employee["department"].lower() == search.lower():
            print(employee)

            found = True

    if not found:
        print("Department not found")

def sort_employees():

    sorted_employees = sorted(employees, key = lambda employee: employee["department"])

    print("\n sorted employees: ")

    for employee in sorted_employees:
        print(employee)

salary_analysis()

average_salary()

sort_employees()

search_department()