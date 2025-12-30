# Polling users about their dream vacation
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

    # Store response
    responses[name] = vacation

    # Ask if another person wants to respond
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Print poll results
print("\n--- Dream Vacation Poll Results ---")
for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")
