# ============================================================
# Python Fundamentals - 05: Lists
# ============================================================

# --- Definition ---
print("\n--- Definition ---")

my_list = list()    # Empty list using constructor
my_other_list = []  # Empty list using literal

print(len(my_list))

my_list = [5, 10, 15, 20, 25]
print(my_list)
print(len(my_list))

my_other_list = [18, "Martin", "Barrero"]

# --- Accessing Elements ---
print("\n--- Accessing Elements ---")

print(my_other_list[0])     #  18       - first element
print(my_other_list[1])     #  "Martin" - second element
print(my_other_list[2])     #  "Barrero"- third element
# my_other_list[3]          -> IndexError: index out of range

print(my_other_list[-1])    #  "Barrero"- last element
print(my_other_list[-2])    #  "Martin" - second to last
print(my_other_list[-3])    #  18       - third to last
# my_other_list[-4]         -> IndexError: index out of range

# --- Search ---
print("\n--- Search ---")

print(my_other_list.count("Martin"))    # 1 - found
print(my_other_list.count("Martín"))    # 0 - accent-sensitive

my_list.append(5)
print(my_list)
print(my_list.count(5))                 # 2 - duplicate found

# --- Unpacking ---
print("\n--- Unpacking ---")

age, name, lastname = my_other_list
print(age)
print(lastname)
# my_other_list[4]          -> IndexError: index out of range

# --- Concatenation ---
print("\n--- Concatenation ---")

print(my_list + my_other_list)

# --- Insert & Update ---
print("\n--- Insert & Update ---")

my_other_list.append("Python")      # Append to end
print(my_other_list)

my_other_list.insert(1, "White")    # Insert at index 1
print(my_other_list)

my_other_list[1] = "Blue"           # Update by index
print(my_other_list)

# --- Removal ---
print("\n--- Removal ---")

my_other_list.remove(18)            # Remove by value
print(my_other_list)
# my_other_list.remove(20)          -> ValueError: value not in list

popped = my_other_list.pop()        # Remove and return last element
print(popped)
print(my_other_list)

popped_at_index = my_other_list.pop(0)  # Remove and return element at index
print(popped_at_index)
print(my_other_list)

del my_other_list[1]                # Delete by index (no return)
print(my_other_list)

# --- List Operations ---
print("\n--- List Operations ---")

my_new_list = my_list.copy()        # Shallow copy
my_list.clear()                     # Empty the original
print(my_new_list)
print(my_list)

my_new_list.reverse()               # In-place reverse
print(my_new_list)

my_new_list.sort()                  # In-place sort (ascending)
print(my_new_list)

# --- Slicing ---
print("\n--- Slicing ---")

print(my_new_list[1:3])             # Elements at index 1 and 2