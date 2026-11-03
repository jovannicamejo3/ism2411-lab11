# Self-Assessment
# 1.
# I would use bracket notation when the key has to be there, like a customer ID, because a `KeyError` tells me right away that something is wrong with the data.
# I would use `.get()` when the field is optional, like a phone number or email, so the program keeps running and uses a default instead of crashing.
# My rule of thumb is brackets for required fields and `.get()` for anything that might be missing.
# 2.
# Building the summary dictionary with a loop reminds me of using SUMIF or a PivotTable in Excel to total sales by region.
# The Python version is more useful for large datasets because it can handle far more rows than Excel's row limit allows.
# It is also repeatable, so I can rerun the same script on new data instead of rebuilding the formulas each time.

print("--Exercise 1--")

customers = [
    {
        "name": "Alice",
        "email": "alice@example.com",
        "tier": "gold",
        "ytd_spend": 12400
    }
]

print(customers[0]["name"])
print(customers[0]["email"])
print(customers[0]["tier"])
print(customers[0]["ytd_spend"])
print(customers[0])

print("--Exercise 2--")

customers[0]['phone'] = "555-5555" #Adding a new key-value pair to the dictionary
print(customers[0])

customers[0]['tier'] = "platinum" #Updating the value of an existing key
print(customers[0])

del(customers[0]["email"]) #Deleting a key-value pair from the dictionary
print(customers[0])

print("--Exercise 3--")

print(customers[0].get('ytd_spend',0))
print(customers[0].get("email", "no email on file"))

try:
    print (customers[0]["email"])
except KeyError as error:
    print(f"KeyError: {error}")

print("--Exercise 4--")

for key, value in customers[0].items():
    print(f"{key}: {value}")        

# Without .items() the loop only gives the keys, so you have to use customers[0][something] to get each value
for something in customers[0]:
    print(something, customers[0][something]) 

print("--Exercise 5--")
tier_discounts = {
    "bronze": 0.00,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
 }

purchase = 200
discount_rate = tier_discounts.get(customers[0]["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customers[0]['tier']}")
print(f"discount rate: {discount_rate * 100}%")
print(f"Final price: ${final_price:.2f}")

print("--Exercise 6--")

customers = [
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "David", "tier": "bronze", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}) - Discount: ${discount:.2f}") # "off a $300 purchase

print("--Exercise 7--")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - Only {product_details['stock']} left")

print("--Exercise 8--")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
    ]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")