# List of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'egg', 'pastrami', 'veggie']

# Empty list for finished sandwiches
finished_sandwiches = []

# Loop through sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print all finished sandwiches
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")
