students = {}

def add_student():

#this creates a loop to enter as many student wanted and type done to stop or break the loop      
     while True:
        name = input("\nEnter student name: ")

        if name.lower() == "done":
            break

#the set in the courses is used to avoid duplication 

        students[name] = {
        "courses": set(),
        "units": 0
    }
        print("student added")

def add_courses():
    name = input("\nEnter student name: ")

    if name in students:
        while True:

            course = input("Enter course for student: ")
            if course.lower() == "done":
                break
            
            units = int(input("Enter course units: "))

            if course not in students[name]["courses"]:

                students[name]["courses"].add(course)
                students[name]["units"] += units

            print("\nCourse added")
    else:
        print("Student not found")

def remove_course():

    name = input("Enter student name: ")

    if name in students:
        course = input("Enter course to remove: ")

        if course in students[name]["courses"]:
            students[name]["courses"].remove(course)
            print ("Course removed")

        else:
            print("Courses not found")

    else:
        print("student not")

def display_students():

    print("\n Student Records:")

    for student in students:
        print("\nName: ", student)
        print("courses: ", students[student]["courses"])
        print("Total unit: ", students[student]["units"])


add_student()

while True:

    print("\n1. Add course")
    print("2. Remove course")
    print("3. View students")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_courses()

    elif choice == "2":
        remove_course()

    elif choice == "3":
        display_students()
#this says run the loop until u choose option 3 or 4
        print("program ended")
        break

    else:
        print("\nInvalid option")