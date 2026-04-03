# ============================================================
# Python Fundamentals - 04: Strings
# ============================================================

name = "Martin"
lastname = "Barrero"
age = 18

# --- Basic Operations ---
print("\n--- Basic Operations ---")

print(len(name))
print(len(lastname))
print(name + " " + lastname)

# --- Escape Characters ---
print("\n--- Escape Characters ---")

my_newline_string = "This is a string\nwith a new line"
print(my_newline_string)

my_tab_string = "\tThis is a string\n\twith tabulation"
print(my_tab_string)

# --- String Formatting ---
print("\n--- String Formatting ---")

print("My name is {} {} and I'm {} years old".format(name, lastname, age))  # .format()
print("My name is %s %s and I'm %d years old" % (name, lastname, age))      # % operator
print("My name is " + name + " " + lastname + " and I'm " + str(age))       # Concatenation
print(f"My name is {name} {lastname} and I'm {age} years old")               # f-string (preferred)

# --- Character Unpacking ---
print("\n--- Character Unpacking ---")

language = "python"
a, b, c, d, e, f = language
print(a)    # p
print(b)    # y
print(f)    # n

# --- Slicing ---
print("\n--- Slicing ---")

print(language[1:5])    # ytho
print(language[0:2])    # py

# Reverse via slicing
reversed_language = language[::-1]
print(reversed_language)    # nohtyp

# --- String Methods ---
print("\n--- String Methods ---")

print(language.capitalize())        # Python  - first letter uppercase
print(language.upper())             # PYTHON  - all uppercase
print(language.lower())             # python  - all lowercase
print(language.count("t"))          # 1       - occurrences of "t"
print(language.isnumeric())         # False   - checks if all chars are numeric
print("123".isnumeric())            # True
print(language.lower().isupper())   # False   - lowercase string is not uppercase
print(language.startswith("py"))    # True
print(language.startswith("Py"))    # False   - case-sensitive
print("Py" == "py")                 # False   - case-sensitive equality