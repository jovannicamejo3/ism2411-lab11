print("--Exercise 1--")

customer = {
    "name": "Alice", #Key : Value ,
    "Name" : "Not-Alice",
    "email" : "alice@exampe.com",
    "tier" : "gold",
    "ytd_spend" : 12400,
}

print(customer["Name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("--Exercise 2--")

customer['phone'] = "555-5555" #Adding a new key-value pair to the dictionary
print(customer)

customer['tier'] = "platinum" #Updating the value of an existing key
print(customer)

del(customer["Name"]) #Deleting a key-value pair from the dictionary]
print(customer)

