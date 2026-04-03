# ============================================================
# Python Fundamentals - 10: Loops
# ============================================================

# --- While ---
print("\n--- While ---")

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Condition is greater than or equal to 10")   # Runs when while exits normally

print("Execution continues...")

# --- While with break ---
print("\n--- While with break ---")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Execution stopped at 15")
        break
    print(my_condition)

print("Execution continues...")

# --- For ---
print("\n--- For ---")

my_list = [18, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Martin", "Barrero", "Python")
for element in my_tuple:
    print(element)

my_set = {"Martin", "Barrero", 18}
for element in my_set:
    print(element)

my_dict = {
    "Name": "Martin",
    "Lastname": "Barrero",
    "Age": 18,
    1: "Python"
}

# --- For with break ---
print("\n--- For with break ---")

for element in my_dict:
    print(element)
    if element == "Age":
        break

print("Execution continues...")

# --- For with continue ---
print("\n--- For with continue ---")

for element in my_dict:
    print(element)
    if element == "Age":
        continue                # Skips the rest of the loop body for this iteration
    print("Executed")
else:
    print("For loop finished normally")

# --- range() ---
print("\n--- range() ---")

for i in range(5):
    print(i)                    # 0, 1, 2, 3, 4

for i in range(2, 10, 2):
    print(i)                    # 2, 4, 6, 8

# --- enumerate() ---
print("\n--- enumerate() ---")

languages = ["Python", "C", "Java"]
for index, value in languages:
    print(f"{index}: {value}")

# --- zip() ---
print("\n--- zip() ---")

names = ["Martin", "Pedro", "Juan"]
ages = [18, 25, 30]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# --- List Comprehension ---
print("\n--- List Comprehension ---")

squares = [x ** 2 for x in range(6)]
print(squares)                              # [0, 1, 4, 9, 16, 25]

even_squares = [x ** 2 for x in range(6) if x % 2 == 0]
print(even_squares)                         # [0, 4, 16]