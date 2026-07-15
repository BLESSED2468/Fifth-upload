"""# Challenge 9 — Match-Case ATM System

Create a terminal ATM menu system.

The menu should support:

1.  Deposit
2.  Withdraw
3.  Check balance
4.  Transfer
5.  Exit

Use `match-case` to control the menu.

----------

## Requirements

-   Use:
    -   Match-case
    -   While loops
    -   Functions
    -   Conditional logic

----------

## Constraints

-   Prevent withdrawing above balance.
-   Prevent negative deposits.
-   Keep running until Exit is selected.

----------"""


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


balance = 1000

def deposit():

    global balance

    amount = float(input("enter deposit amount: "))

    if amount >0:
        balance += amount
        print("deposit successful")

    else:
        print("invalid deposit")

def withdraw():

    global balance 

    amount = float(input("enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        print("withdrawal successful")

    else:
        print("insufficient balance")

def check_balance():

    print("balance:", balance)

while True:

    print("\n1. deposit")
    print("2. withdraw")
    print("3. check balance")
    print("4. exit")

#instead of using if/else we use the switch statement which reads the number typed by the user and jumps to the matching case 
    choice = int(input("\nchoose option: "))

    match choice:
        case 1:
            deposit()

        case 2:
            withdraw()

        case 3:
            check_balance()

        case 4:
            print("\exiting...")
            break

        case _:
            print("invalid option")