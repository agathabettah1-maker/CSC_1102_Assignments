# Exercise 3-4: Guest List
guests = ["Joyce", "Martin", "Clara"]

# Print invitations without using loops
list(map(lambda g: print(f"Dear {g}, you are invited to dinner."), guests))

# Exercise 3-5: Changing Guest List
print("\nUnfortunately, Joyce can't make it to the dinner.")

# Replace Joyce with Samuel
guests[0] = "Samuel"

list(map(lambda g: print(f"Dear {g}, you are still invited to dinner."), guests))

# Exercise 3-6: More Guests
print("\nGood news! I found a bigger dinner table, so more guests can join.")

# Insert guests at beginning, middle, and end
guests.insert(0, "Linda")
guests.insert(len(guests)//2, "Peter")
guests.append("Nora")

list(map(lambda g: print(f"Dear {g}, you are invited to dinner."), guests))

# Exercise 3-7: Shrinking Guest List
print("\nBad news! The new dinner table won't arrive in time, "
      "so I can only invite two people.")

# Pop until only two remain
while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed}, I can't invite you to dinner.")

# Print remaining invitations
list(map(lambda g: print(f"Dear {g}, you are still invited to dinner."), guests))

# Clear the list
guests.clear()
print("\nFinal guest list:", guests)
