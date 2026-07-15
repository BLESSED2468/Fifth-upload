"""
## Task 6 — Password Pattern Inspector

### Scenario

A security company wants a quick password inspection tool.

### Concepts Practiced

- Booleans
- Membership operators
- Strings
- Comparison operators

### Requirements

Ask the user for a password.

Display whether:

- it contains `"@"`
- it contains numbers like `"1"`
- its length is greater than 8

### Example Output

```python
Contains @: True
Contains 1: False
Long Password: True
```

### Brain Task

You must use:

- membership operators (`in`)
- comparisons
- boolean values

### Checklist

-  Uses `in`
-  Uses booleans
-  Uses `len()`
-  Includes comments"""

passward = input("Enter a passward ")

contains_first= "@" in passward
contains_second = "1>=9" in passward
contains_third = len(passward) >8

print("Contains @:", contains_first)
print("Contains 1:" ,contains_second)
print("Long Password:" ,contains_third)