## Task 2 — E-Commerce Discount Calculator
# in this task the company wants to show hw much their customers has saved through discount
"""Ask the user for:

- Product name
- Original price
- Discount percentage"""

product = input("Enter product name: ")
price = float(input("enter the original price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = (discount/100)*price

final_price = price -  discount_amount

print("="*10, "PURCHASE SUMMARY", "="*10)
print("Product:", product)
print("OG price:", price)
print("Discount: ", discount_amount)
print("Final price: ", final_price)

