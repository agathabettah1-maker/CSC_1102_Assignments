# Sandwich orders with pastrami appearing multiple times
sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'egg', 'pastrami', 'veggie']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")

# Remove all occurrences of 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process remaining orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print all finished sandwiches
print("\nAll sandwiches have been made (no pastrami):")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")
