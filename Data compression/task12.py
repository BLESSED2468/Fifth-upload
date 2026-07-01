"""## Task 12 — Intern Data Compression Challenge

### Scenario

A tech company wants to create short compressed tags for intern records.

### Concepts Practiced

- Strings
- Slicing
- Lists
- Formatting

### Requirements

Ask the user for:

- Full name
- Department
- State
- Favorite programming language

Generate a compressed tag using:

- first 2 letters of name
- first 2 letters of department
- first 2 letters of state
- first 2 letters of programming language

Store all pieces in a list before combining them.

### Example

Input:

```python
Samuel
Software Engineering
Lagos
Python
```

Output:

```python
Compressed Tag: SASOLApy
```

### Brain Task

You must:

- slice multiple strings
- store pieces in a list
- combine them correctly

### Checklist

-  Uses lists
-  Uses slicing
-  Uses string combination
-  Includes comments"""


name = input("Enter your full name: ")
department = input("Enter your department: ")
state = input("Enter your state of origin: ")
favourite = input("Enter your favourite programming language: ")

list = []

name_letter = list.append(name[:2])
department_letter = list.append(department[:2])
state_letter = list.append(state[:2])
favourite = list.append(favourite[:2])

clean = list[0] + list[1] + list[2] + list[3]

print("Compressed Tag: ", clean)