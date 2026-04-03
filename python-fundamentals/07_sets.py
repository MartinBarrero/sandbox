# ============================================================
# Python Fundamentals - 07: Sets
# ============================================================

# --- Definition ---
print("\n--- Definition ---")

my_set = set()      # Empty set using constructor
my_other_set = {}   # This is a dict, not a set!

print(type(my_set))         # <class 'set'>
print(type(my_other_set))   # <class 'dict'> - empty {} defaults to dict

my_other_set = {"Martin", "Barrero", 18}    # Now it is a set
print(type(my_other_set))   # <class 'set'>
print(len(my_other_set))

# --- Insertion ---
print("\n--- Insertion ---")

my_other_set.add("Python")
my_other_set.add("a")
print(my_other_set)     # Sets are unordered - output order may vary

my_other_set.add("Python")  # Duplicates are ignored
print(my_other_set)

# --- Search ---
print("\n--- Search ---")

print("Martin" in my_other_set)     # True  - case-sensitive
print("martin" in my_other_set)     # False - case-sensitive

# --- Removal ---
print("\n--- Removal ---")

my_other_set.remove("Martin")   # Remove by value
print(my_other_set)

my_other_set.clear()            # Empty the set
print(len(my_other_set))        # 0

del my_other_set                # Delete the entire variable
# print(my_other_set)           -> NameError: name 'my_other_set' is not defined

# --- Conversion ---
print("\n--- Conversion ---")

my_set = {"Martin", "Barrero", 18}
my_list = list(my_set)      # Convert set to list to enable indexing
print(my_list)
print(my_list[0])

# --- Set Operations ---
print("\n--- Set Operations ---")

my_other_set = {"Java", "C", "Python"}

my_new_set = my_set.union(my_other_set)             # Combines both sets
print(my_new_set)

print(my_new_set.union(my_new_set)                  # Chained union
      .union(my_set)
      .union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))                # Elements in my_new_set not in my_set