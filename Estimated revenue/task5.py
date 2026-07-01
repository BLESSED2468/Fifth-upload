""" Task 5 — Movie Ticket Revenue Estimator

### Scenario

A cinema wants to estimate revenue from ticket sales.

### Concepts Practiced

- Arithmetic operators
- Variables
- Formatting
- Numbers

### Requirements

Ask the user for:

- Number of regular tickets sold
- Number of VIP tickets sold

Prices:

- Regular = ₦2500
- VIP = ₦5000

Calculate:

- Revenue from regular tickets
- Revenue from VIP tickets
- Total revenue

### Example Output

```python
===== SALES REPORT =====
Regular Revenue: ₦15000
VIP Revenue: ₦20000
Total Revenue: ₦35000
```

### Brain Task

Break the problem into smaller calculations.

### Checklist

-  Uses multiple calculations
-  Uses meaningful variables
-  Uses formatting
-  Includes comments
"""

regular_tickets = int(input("enter the number of tickets sold "))
vip_tickets = int(input("Enter the total number of vip tickets sold "))

regular_prices = 2500
vip_prices = 5000

regular_tickets_revenue = regular_tickets * regular_prices
vip_tickets_revenue = vip_tickets * vip_prices 

total_revenue = regular_tickets_revenue + vip_tickets_revenue

print("="*10, "SALES REVENUE" , "="*10)
print("Regular Revenue: ", regular_tickets_revenue)
print("Vip Revenue: ", vip_tickets_revenue)
print("Total Revenue: ", total_revenue)