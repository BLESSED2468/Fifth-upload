"""Task 8 — Fake Bank Account Masking System

### Scenario

A banking app wants to hide customer account numbers.

### Concepts Practiced

- String slicing
- Concatenation
- String length
- Formatting

### Requirements

Ask the user for:

- Account number

Display:

- first 2 digits visible
- last 2 digits visible
- middle digits replaced with `"******"`

### Example

Input:

```python
1234567890
```

Output:

```python
12******90
```

### Brain Task

Think carefully about:

- beginning slice
- ending slice
- combining pieces

### Checklist

-  Uses slicing
-  Uses concatenation
-  Produces formatted output
-  Includes comments"""


user_password = input("Enter your password ")

first_part = user_password[:2]

second_part = user_password[-2:]


password_security = first_part[:2] + "******" + second_part[-2:]

print(password_security)




