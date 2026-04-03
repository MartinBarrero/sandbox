# ============================================================
# Python Fundamentals - 03: Operators
# ============================================================

# --- Arithmetic Operators ---
print("\n--- Arithmetic Operators ---")

print(3 + 4)    # Addition
print(3 - 4)    # Subtraction
print(3 * 4)    # Multiplication
print(3 / 4)    # Division
print(10 % 3)   # Modulo
print(10 // 3)  # Floor division
print(2 ** 3)   # Exponentiation

# Operator precedence example
print(2 ** 3 + 3 - 7 / 1 // 4)

# --- String Operators ---
print("\n--- String Operators ---")

print("Hello " + "Python " + "How are you?")   # Concatenation
print("Hello " + str(5))                        # Concatenation with type casting

# --- Mixed Operators ---
print("\n--- Mixed Operators ---")

print("Hello " * 5)                # Repetition
print("Hello " * (2 ** 3))         # Repetition with expression

my_float = 2.5 * 2
print("Hello " * int(my_float))    # Repetition with type casting

# --- Comparison Operators ---
print("\n--- Comparison Operators ---")

print("a" < "z")                       # Alphabetical comparison (ASCII)
print("Hello" > "Python")
print("Hello" < "Python")
print("aaaa" > "abaa")                 # Character-by-character ASCII comparison
print(len("aaaa") >= len("abaa"))      # Length comparison
print("Hello" <= "Python")
print("Hello" == "Hello")              # Equality
print("Hello" != "Python")             # Inequality

# --- Logical Operators ---
print("\n--- Logical Operators ---")

print(3 > 4 and "Hello" > "Python")                        # and: both must be True
print(3 > 4 or "Hello" > "Python")                         # or: at least one must be True
print(3 < 4 and "Hello" < "Python")
print(3 < 4 or "Hello" > "Python")
print(3 < 4 or ("Hello" > "Python" and 4 == 4))            # Grouped logic
print(not (3 > 4))                                          # not: negation