# ============================================================
# Python Fundamentals - 09: Conditionals
# ============================================================

# --- if ---
print("\n--- if ---")

my_condition = False

if my_condition:        # Equivalent to: if my_condition == True
    print("The if condition is executed")

my_condition = 5 * 5   # 25

if my_condition == 10:
    print("The second if condition is executed")

# --- if, elif and else ---
print("\n--- if, elif and else ---")

if my_condition > 10 and my_condition < 20:
    print("Greater than 10 and less than 20")
elif my_condition == 25:
    print("Equal to 25")
else:
    print("Less than or equal to 10, or greater than or equal to 20, and not equal to 25")

print("Execution continues...")

# --- Truthy and Falsy Values ---
print("\n--- Truthy and Falsy Values ---")

# Falsy values in Python: False, 0, 0.0, "", [], {}, set(), tuple(), None
print(bool(""))         # False - empty string
print(bool("Martin"))   # True  - non-empty string
print(bool(0))          # False - zero
print(bool(42))         # True  - non-zero
print(bool([]))         # False - empty list
print(bool([1, 2]))     # True  - non-empty list

# --- Value Inspection ---
print("\n--- Value Inspection ---")

my_string = ""

if not my_string:               # True when my_string is falsy (empty)
    print("The string is empty")

my_string = "Martin"

if my_string == "Martin":
    print("The strings match")

# --- Ternary Operator ---
print("\n--- Ternary Operator ---")

age = 20
status = "adult" if age >= 18 else "minor"
print(status)

# --- Chained Comparisons ---
print("\n--- Chained Comparisons ---")

value = 15
print(10 < value < 20)          # True  - pythonic range check
print(10 < value < 14)          # False

# --- Match / Case (Python 3.10+) ---
print("\n--- Match / Case ---")

language = "Python"

match language:
    case "Python":
        print("You chose Python")
    case "Java":
        print("You chose Java")
    case "C" | "C++":          # Multiple values with |
        print("You chose C or C++")
    case _:                    # Default case
        print("Unknown language")