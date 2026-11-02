inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# --- Exercise 1 ---

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory[0])

print(inventory[-1])

middle_index = len(inventory) // 2
print(inventory[middle_index])

# --- Exercise 2 ---

print(inventory[3])
print(inventory[-2])
print(inventory[::2])

# --- Exercise 3 ---

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# --- Exercise 4 ---

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples are immutable, so you cannot change their values.")