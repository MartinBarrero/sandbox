# ============================================================
# Python Fundamentals - 08: Dictionaries
# ============================================================

# --- Definition ---
print("\n--- Definition ---")

my_dict = dict()    # Empty dict using constructor
my_other_dict = {}  # Empty dict using literal

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Name": "Martin",
    "Lastname": "Barrero",
    "Age": 18,
    1: "Python"
}

my_dict = {
    "Name": "Martin",
    "Lastname": "Barrero",
    "Age": 18,
    "Languages": {"Python", "C", "C++"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

# --- Search ---
print("\n--- Search ---")

print(my_dict[1])
print(my_dict["Name"])          # Access value by key

print("Martin" in my_dict)      # False - checks keys, not values
print("Lastname" in my_dict)    # True
print("Age" in my_dict)         # True
print(18 in my_dict)            # False - 18 is a value, not a key

# --- Insertion ---
print("\n--- Insertion ---")

my_dict["Street"] = "12th Street"
print(my_dict)

# --- Update ---
print("\n--- Update ---")

my_dict["Name"] = "Pedro"
print(my_dict["Name"])

# --- Removal ---
print("\n--- Removal ---")

del my_dict["Street"]
print(my_dict)

# --- Dictionary Methods ---
print("\n--- Dictionary Methods ---")

print(my_dict.items())      # Key-value pairs as tuples
print(my_dict.keys())       # All keys
print(my_dict.values())     # All values

# --- fromkeys() ---
print("\n--- fromkeys() ---")

my_list = ["Name", 1, "Floor"]

my_new_dict = dict.fromkeys(my_list)        # Keys from list, values default to None
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)        # Keys from another dict, values default to None
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, 1)     # Keys from another dict, all values set to 1
print(my_new_dict)

# --- Type Conversion ---
print("\n--- Type Conversion ---")

my_values = my_new_dict.values()
print(type(my_values))                                          # <class 'dict_values'>
print(my_new_dict.values())

print(list(dict.fromkeys(list(my_new_dict.values())).keys()))   # Deduplicate values using fromkeys
print(tuple(my_new_dict))                                       # Tuple of keys
print(set(my_new_dict))                                         # Set of keys