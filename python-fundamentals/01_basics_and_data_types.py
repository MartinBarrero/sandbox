# ============================================================
# Python Fundamentals - 01: Basics and Data Types
# ============================================================

# --- Printing & Basic Operations ---

print("Hello World")

print(5 ** 2)   # Exponentiation
print(3 % 2)    # Modulo
print(3 // 2)   # Floor division

# --- Data Types ---

print(type("Hello World"))                      # str
print(type(5))                                  # int
print(type(0.5))                                # float
print(type([0, 11, 5, 58]))                     # list
print(type({"name": "Martin", "id": "123"}))    # dict
print(type({1.5, 3.14, 2.7}))                   # set
print(type((1.5, 3.14, 2.7)))                   # tuple
print(type(True))                               # bool
print(type(None))                               # NoneType

# --- Notes: Grouped Data Types ---

# 1. List    -> Ordered, mutable, allows duplicates. Similar to a dynamic array.
# 2. Dict    -> Key-value pairs. Keys must be unique.
# 3. Set     -> Unordered, no duplicates, no indexing.
# 4. Tuple   -> Ordered, immutable. Similar to a fixed array.