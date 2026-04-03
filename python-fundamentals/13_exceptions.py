# ============================================================
# Python Fundamentals - 13: Exception Handling
# ============================================================

number_one = 5
number_two = "1"       # Intentional type mismatch to trigger TypeError

# --- Basic Exception Handling: try and except ---
print("\n--- Basic Exception Handling: try and except ---")

try:
    print(number_one + number_two)
    print("No error occurred")
except:
    print("An error occurred")

# --- Full Exception Flow: try, except, else and finally ---
print("\n--- Full Exception Flow: try, except, else and finally ---")

try:
    print(number_one + number_two)
    print("No error occurred")
except:
    print("An error occurred")
else:
    # Runs only if no exception was raised
    print("Execution continued successfully")
finally:
    # Always runs regardless of whether an exception occurred
    print("Finally block always executes")

# --- Catching Specific Exception Types ---
print("\n--- Catching Specific Exception Types ---")

try:
    print(number_one + number_two)
    print("No error occurred")
except ValueError:
    print("A ValueError occurred")
except TypeError:
    print("A TypeError occurred")      # This one will trigger

# --- Capturing Exception Information ---
print("\n--- Capturing Exception Information ---")

try:
    print(number_one + number_two)
    print("No error occurred")
except ValueError as error:
    print(error)                        # Prints the error message
except Exception as error:             # Catches any other exception type
    print(error)

# --- Raising Exceptions ---
print("\n--- Raising Exceptions ---")

def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

try:
    print(divide(10, 2))       # 5.0
    print(divide(10, 0))       # Raises ValueError
except ValueError as error:
    print(error)

# --- Custom Exceptions ---
print("\n--- Custom Exceptions ---")

class NegativeValueError(Exception):    # Inherits from Exception
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative values are not allowed: {value}")

def square_root(number):
    if number < 0:
        raise NegativeValueError(number)
    return number ** 0.5

try:
    print(square_root(9))       # 3.0
    print(square_root(-4))      # Raises NegativeValueError
except NegativeValueError as error:
    print(error)

# --- Catching Multiple Exceptions in One Line ---
print("\n--- Catching Multiple Exceptions in One Line ---")

try:
    value = int("not a number")
except (ValueError, TypeError) as error:
    print(f"Caught: {error}")