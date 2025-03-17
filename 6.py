import math
import datetime
import sys
import importlib
import types

# ------------------------------
# 1. Using built-in modules (math and datetime)
number = 25
square_root = math.sqrt(number)
print("Square root of", number, "is", square_root)

current_date = datetime.datetime.now()
print("Current date and time:", current_date)

# ------------------------------
# 2. Creating and using a custom module (inline)
def greet(name):
    return f"Hello, {name}!"

print(greet("Debdoot"))

# ------------------------------
# 3. Working with a package
# We'll simulate a package by creating a module-type object for 'mypackage'
mypackage = types.ModuleType("mypackage")
mypackage.submodule = types.ModuleType("submodule")

def add(a, b):
    return a + b

mypackage.submodule.add = add
print("Sum using package submodule (mypackage.submodule.add):", mypackage.submodule.add(3, 4))

# ------------------------------
# 4. Checking if a package is installed and using it (using 'requests')
try:
    import requests
except ImportError:
    print("The 'requests' package is not installed. Please install it using 'pip install requests'.")
else:
    response = requests.get("https://api.github.com")
    print("GitHub API status code (using requests):", response.status_code)

# ------------------------------
# 5. Using sys to manipulate the module search path
sys.path.append("/path/to/your/directory")
print("Updated sys.path with '/path/to/your/directory'.")

# ------------------------------
# 6. Reloading a module after making changes
# To simulate reloading, we create a dummy 'custom_module' using types.ModuleType.
custom_module = types.ModuleType("custom_module")
custom_module.greet = greet  # Assign the previously defined greet function
# Register the module in sys.modules so that importlib.reload can work properly.
sys.modules["custom_module"] = custom_module

# Reload the module (this won't change behavior here as the module remains the same)
importlib.reload(custom_module)
print("Reloaded custom_module greet function:", custom_module.greet("Debdoot"))