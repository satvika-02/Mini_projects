cart = ["Rice", "Milk", "Bread"]

print("Original Cart:", cart)

# Add a product
cart.append("Eggs")
print("After adding Eggs:", cart)

# Add a product at a specific position
cart.insert(1, "Sugar")
print("After inserting Sugar:", cart)

# Remove a product
cart.remove("Milk")
print("After removing Milk:", cart)

# Remove the last product
cart.pop()
print("After pop:", cart)

# Sort the cart
cart.sort()
print("Sorted Cart:", cart)

# Reverse the cart
cart.reverse()
print("Reversed Cart:", cart)