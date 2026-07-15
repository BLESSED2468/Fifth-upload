"""Challenge 11 — Recursive Folder Size Calculator

Simulate a folder structure using nested dictionaries.

Example:

```python
{
    "Documents": {
        "python.pdf": 120,
        "notes.txt": 30
    }
}

```

Create a recursive function that:

1.  Traverses the structure.
2.  Calculates total file size.
3.  Counts total files.
4.  Finds the largest file.

----------

## Requirements

-   Use:
    -   Recursion
    -   Dictionaries
    -   Functions

----------

## Constraints

-   You must use recursion.
-   No global variables.

----------

# General Rules

For every task:

1.  Use meaningful variable names.
2.  Break logic into functions where possible.
3.  Avoid unnecessary repeated code.
4.  Handle invalid inputs where reasonable.
5.  Keep output readable and organized.
6.  Add comments explaining difficult sections.
7.  Test your program with multiple inputs.

### Do not rush to code immediately.

Before writing any code:
1.  Understand the problem.
2.  Identify the data structures needed.
3.  Plan your functions.
4.  Think about edge cases.
5.  Then begin implementation.

"""


#this is a dictionary that with two keys: doucment and picture

folder = {
    "documents": {
        "python.pdf":120,
        "notes.txt": 30
    },
    "pictures": {
        "image.jpg": 200,
        "photo.png": 150
    }
}

def calculate_folder(data):

    total_size = 0
    total_files = 0

#this holds a pair of all
    largest_file = ("", 0)

    for key, value in data.items():

        if isinstance(value, dict):

            size, files, largest = calculate_folder(value)

            total_size += size
            total_files += files

            if largest[1] > largest_file[1]:
                largest_file = largest

        else: 
            total_size += value
            total_files += 1

            if value > largest_file[1]:
                largest_file = (key, value)

    return total_size, total_files, largest_file

size, files, largest = calculate_folder(folder)

print("total size:", size)
print("total files:", files)
print("largest file:", largest)