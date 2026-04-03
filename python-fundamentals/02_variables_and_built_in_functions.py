# ============================================================
# Python Fundamentals - 02: Variables and Built-in Functions
# ============================================================

# --- Naming Conventions ---
print("\n--- Naming Conventions ---")

variable = "Lowercase variable"
my_variable = "Snake case variable"
MY_CONSTANT = "Upper snake case constant"   # Constants by convention
my_int_variable = 5

print(variable)
print(my_variable)
print(MY_CONSTANT)
print(my_int_variable)

# --- Type Casting ---
print("\n--- Type Casting ---")

name = "Martin"
age = 18

print(type(age))
age = str(age)      # int -> str
print(type(age))

# --- F-Strings ---
print("\n--- F-Strings ---")

name = "Martin"
age = 18

print(f"Hi, my name is {name} and I'm {age} years old")
print(f"In 5 years I will be {age + 5} years old")      # Expressions inside f-strings
print(f"{'Martin':>10}")                                 # Right-aligned with width 10
print(f"{3.14159:.2f}")                                  # Float formatting

# --- Multiple Assignment ---
print("\n--- Multiple Assignment ---")

a, b, c = 1, 2, 3
print(a, b, c)

x = y = z = 0       # Assign the same value to multiple variables
print(x, y, z)

# --- Swap ---
print("\n--- Swap ---")

a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# --- Augmented Assignment ---
print("\n--- Augmented Assignment ---")

counter = 0
counter += 1    # counter = counter + 1
print(counter)

counter -= 1    # counter = counter - 1
print(counter)

counter *= 5    # counter = counter * 5
print(counter)

counter //= 2   # counter = counter // 2
print(counter)

# --- Type Checking ---
print("\n--- Type Checking ---")

value = 42
print(type(value))
print(isinstance(value, int))           # True
print(isinstance(value, (int, float)))  # Checks against multiple types

# --- None ---
print("\n--- None ---")

result = None
print(result)
print(type(result))
print(result is None)       # Correct way to check for None
print(result is not None)

# --- Built-in Functions ---
print("\n--- Built-in Functions ---")

name = "Martin"
name_length = len(name)
print(f"{name} has {name_length} characters")

name = input("Enter your name: ")
print(f"Hello, {name}!")