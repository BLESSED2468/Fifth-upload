"""Task 9 — Mini Payroll Estimator

### Scenario

A startup company wants to estimate employee salary payouts.

### Concepts Practiced

- Arithmetic operators
- Variables
- Casting
- Formatting

### Requirements

Ask the user for:

- Employee name
- Hours worked
- Pay per hour
- Tax percentage

Calculate:

- Gross pay
- Tax amount
- Net pay

### Example Output

```python
===== PAYROLL =====
Employee: David

Gross Pay: ₦80000
Tax: ₦8000
Net Pay: ₦72000
```"""

user_name = (input("Enter your name"))
work_hour = int(input("Enter the number of hours worked"))
hourly_pay = float(input("Enter how much you earn per hour"))
tax_percentage = float(input("Enter total tax percentage"))

gross_pay = work_hour *hourly_pay
 
Tax = (tax_percentage/100)*gross_pay

Net_pay = gross_pay - Tax

print("="*5, "PAY ROLL", "="*5)
print("Employee")
print("Gross pay: ", gross_pay)
print("Tax: ", Tax)
print("Net Pay: ", Net_pay)