# ============================================================
# Python Fundamentals - 06: Tuples
# ============================================================

# --- Definition ---
print("\n--- Definition ---")

my_tuple = tuple()      # Empty tuple using constructor
my_other_tuple = ()     # Empty tuple using literal

my_tuple = (18, 1.75, "Martin", "Barrero")
my_other_tuple = (5, 10, 15, 20, 25)

print(my_tuple)
print(type(my_tuple))

# --- Accessing Elements and Search ---
print("\n--- Accessing Elements and Search ---")

print(my_tuple[2])      # "Martin" - third element
print(my_tuple[0])      # 18       - first element
print(my_tuple[-1])     # "Barrero"- last element
# my_tuple[4]           -> IndexError: index out of range

print(my_tuple.count("Martin"))     # 1 - occurrences of "Martin"
print(my_tuple.index("Martin"))     # 2 - index of first occurrence

# my_tuple[1] = 1.80    -> TypeError: tuples are immutable

# --- Concatenation ---
print("\n--- Concatenation ---")

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# --- Slicing ---
print("\n--- Slicing ---")

print(my_sum_tuple[3:6])    # Elements at index 3, 4 and 5

# --- Mutable Conversion ---
print("\n--- Mutable Conversion ---")

# Tuples are immutable, but can be converted to a list to modify them
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[0] = "Python"      # Update by index
my_tuple.insert(1, "Blue")  # Insert at index 1
print(my_tuple)

my_tuple = tuple(my_tuple)  # Convert back to tuple
print(my_tuple)
print(type(my_tuple))

# --- Deletion ---
print("\n--- Deletion ---")

# del my_tuple[2]   -> TypeError: tuple object does not support item deletion

del my_tuple        # Delete the entire variable
# print(my_tuple)   -> NameError: name 'my_tuple' is not defined