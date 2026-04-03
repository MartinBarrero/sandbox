# ============================================================
# Python Fundamentals - 14: Modules
# ============================================================

# --- Importing a Custom Module ---
print("\n--- Importing a Custom Module ---")

import math_utils

math_utils.sum_values(5, 3, 2)
math_utils.print_value("Hello Python")

# --- Importing Specific Functions ---
print("\n--- Importing Specific Functions ---")

from math_utils import sum_values, print_value

print(sum_values(1, 2, 3))      # Called directly without module prefix
print_value("Imported directly")

# --- Importing with Alias ---
print("\n--- Importing with Alias ---")

import math_utils as mu         # Alias to shorten module reference

mu.print_value("Using alias")

# --- Importing from Standard Library ---
print("\n--- Importing from Standard Library ---")

import math

print(math.pi)                  # 3.141592653589793
print(math.pow(2, 8))           # 256.0
print(math.sqrt(16))            # 4.0
print(math.floor(3.9))          # 3
print(math.ceil(3.1))           # 4
print(math.factorial(5))        # 120

# --- Other Useful Standard Library Modules ---
print("\n--- Other Useful Standard Library Modules ---")

import random

print(random.randint(1, 10))            # Random int between 1 and 10
print(random.choice(["Python", "C", "Java"]))   # Random element from list

import os

print(os.getcwd())                      # Current working directory
print(os.path.exists("math_utils.py")) # Check if file exists