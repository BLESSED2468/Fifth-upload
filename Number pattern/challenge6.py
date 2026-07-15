"""Challenge 6 — Smart Number Pattern Generator

Create a pattern generator using loops and ranges.

The program should:

1.  Ask the user for a number `n`.
2.  Generate:
    -   Even numbers from 1 to n
    -   Odd numbers from 1 to n
    -   Multiples of 3
3.  Store each category in separate lists using list comprehension.
4.  Display the lists.
5.  Display the sum of each category.

----------

## Requirements

-   Use:
    -   Range
    -   List comprehension
    -   Loops
    -   Functions

----------

## Assessment Criteria

-   Proper list comprehension
-   Efficient looping
-   Proper categorization

----------"""


def generate_patterns(n):
#This comprehension list and instead of writing long blocks of code it enables us to write it in a line  
    evens = [num for num in range(1, n + 1) if num % 2 ==0]
    odds = [num for num in range(1, n + 1) if num % 2 !=0]

    multiples_of_3 = [num for num in range(1, n + 1) if num % 3 == 0]

    print("even numbers:", evens)
    print("odd numbers:", odds)
    print("multiples of 3:", multiples_of_3)

    print("\n sum of even numbers:", sum(evens))
    print("sum of odd numbers: ", sum(odds))
    print("sum of multiples of 3: ", sum(multiples_of_3))

number = int(input("Enter a number: "))

