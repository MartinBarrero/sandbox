# ============================================================
# Python Fundamentals - 11: Functions
# ============================================================

# --- Definition ---
print("\n--- Definition ---")

def my_function():
    print("This is a function")

my_function()
my_function()
my_function()

# --- Parameters and Arguments ---
print("\n--- Parameters and Arguments ---")

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(20, 30)          # int
sum_two_values(54754, 71231)    # int
sum_two_values("5", "7")        # str - concatenates instead of adding
sum_two_values(1.4, 5.2)        # float

# --- Return Value ---
print("\n--- Return Value ---")

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(1.4, 5.2)
print(my_result)

# --- Keyword Arguments ---
print("\n--- Keyword Arguments ---")

def print_name(name, lastname):
    print(f"{name} {lastname}")

print_name("Martin", "Barrero")
print_name(lastname="Barrero", name="Martin")   # Order does not matter with keyword args

# --- Default Parameters ---
print("\n--- Default Parameters ---")

def print_name_with_default(name, lastname, alias="No alias"):
    print(f"{name} {lastname} - Alias: {alias}")

print_name_with_default("Martin", "Barrero")            # alias uses default value
print_name_with_default("Martin", "Barrero", "Tin")     # alias overridden

# --- Arbitrary Arguments (*args) ---
print("\n--- Arbitrary Arguments (*args) ---")

def print_upper_texts(*texts):      # Accepts any number of positional arguments
    print(type(texts))              # <class 'tuple'>
    for text in texts:
        print(text.upper())

print_upper_texts("hello", "goodbye", "python")     # Passed as individual args, not a list

# --- Arbitrary Keyword Arguments (**kwargs) ---
print("\n--- Arbitrary Keyword Arguments (**kwargs) ---")

def print_person_info(**kwargs):    # Accepts any number of keyword arguments
    print(type(kwargs))             # <class 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_info(name="Martin", age=18, language="Python")

# --- Multiple Return Values ---
print("\n--- Multiple Return Values ---")

def min_and_max(numbers):
    return min(numbers), max(numbers)   # Returns a tuple

minimum, maximum = min_and_max([4, 1, 9, 2, 7])
print(f"Min: {minimum}, Max: {maximum}")

# --- Type Hints ---
print("\n--- Type Hints ---")

def add(a: int, b: int) -> int:
    return a + b

print(add(3, 5))

def greet(name: str, age: int) -> str:
    return f"Hi, I'm {name} and I'm {age} years old"

print(greet("Martin", 18))

# --- Lambda Functions ---
print("\n--- Lambda Functions ---")

square = lambda x: x ** 2
print(square(5))                        # 25

add = lambda x, y: x + y
print(add(3, 4))                        # 7

numbers = [4, 1, 9, 2, 7]
print(sorted(numbers, key=lambda x: x))            # Ascending
print(sorted(numbers, key=lambda x: -x))           # Descending