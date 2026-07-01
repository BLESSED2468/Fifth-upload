"""Challenge 4 — Inventory Dictionary Manager

Create a mini inventory system.

Each product should contain:

```python
{
    "name": "",
    "price": 0,
    "quantity": 0
}

```

The program should:

1.  Allow the user to add 5 products.
2.  Store them in a dictionary.
3.  Display:
    -   Total inventory value
    -   Product with highest quantity
4.  Allow updating a product quantity.
5.  Remove products with quantity equal to 0.

----------

## Requirements

-   Use:
    -   Nested dictionaries
    -   Loops
    -   Functions
    -   If statements

----------

## Assessment Criteria

-   Proper nested dictionary structure
-   Correct update logic
-   Correct removal logic
-   Good function decomposition

----------"""

"""#this is an empty dictinary where every product will be stored
inventory = {}

#we create a function called add_product because instead of rewriting a code many time its easier to store them in a function
def add_product():
#create a loop to run 5 times as specified in the instruction,which means the user can enter only 5 product
    for i in range(5):
        product_id = input("\nEnter product ID: ")

        name = input("Enter  product name: ")
        price = float(input("enter product price: "))
        quantity = int(input("Enter quantity: "))
#this creates a nested dictionary  
        inventory[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
#then create another function to calculate the total value of all product
def total_inventory_value():
    #after calculating the total value of inventory it stores it here  
    total = 0
#this loops through the inventory_value  and gets only product data
    for product in inventory.values():
                #this calculates the product value
                total += product["price"]* product["quantity"]

    return total
        
def highest_quantity_product():
    highest = max(inventory, key=lambda x: inventory[x]["quantity"])

    return inventory[highest]["name"]

#this function here what it does is, it changes product quantity 
def update_quantity():

    #this enables the user to choose the product they want to update
    product_id = input("\nEnter product id to update: ")

#this checks if the product the user want to changes exists in the inventory
    if product_id in inventory:
        #this is where we get the new quantity update from the user
        new_quantity = int(input("enter new quantity"))
        #this changes the old quantity into the new quantity
        inventory[product_id]["quantity"] = new_quantity




#removes product that are out of stock and stores it in the remove list to delete later
def remove_zero_quantity():
    remove_list = []

    for product_id, product in inventory.items():
        if product["quantity"] == 0:
            remove_list.append(product_id)

#
    for product_id in remove_list:
        #del removes items from dictionary completely
        del inventory[product_id]

add_product()
#runs and add product function

print("\n total inventory value: ", total_inventory_value())
print("highest quantity product: ", highest_quantity_product())

update_quantity()
#updatesquantity

remove_zero_quantity()
#removes zero stock items

print("\n updated inventory: ")
print(inventory[product][quantity])"""

inventory = {}

def add_products():
    
    for i in range(5):
        print(f"\nproduct  {i + 1}")

        name = input("enter product name: ")
        price = float(input("enter product price: "))
        quantity = int(input("enter product quantity: "))

        inventory[name] = {
            "price":price,
            "quantity":quantity
        }
    
def total_inventory_value():
    total = 0

    for product in inventory:
        price= inventory[product]["price"]

        quantity = inventory[product]["quantity"]

        total+= price*quantity

    print("\ntotal inventory value: ", total)

def highest_quantity():
    highest = max(inventory, key=lambda product: inventory[product]["quantity"])

    print("\nproduct with highest quantity: ")
    print(highest)
    print("quantity:", inventory[highest]["quantity"])

def update_quantity():
    product = input("\nenter product to indicate: ")

    if product in inventory:
        new_quantity = int(input("enter new quantity: "))

        inventory[product]["quantity"] = new_quantity

        print("\nupdate quantity: ")
        print(inventory[product]["quantity"])

    else:
        print("product not found")

"""def remove_zero_quantity():
    remove_list = []

    for product in inventory.items():
        if product("quantity") == 0:
            remove_list.append(product)

    for product in remove_list:
        del inventory[product]

        print("\nupdated inventory: ")
        print(inventory)


        remove_list = []

    for product_id, product in inventory.items():
        if product["quantity"] == 0:
            remove_list.append(product_id)

#
    for product_id in remove_list:
        #del removes items from dictionary completely
        del inventory[product_id]"""



add_products()

total_inventory_value()

highest_quantity()

update_quantity()

#remove_zero_quantity()