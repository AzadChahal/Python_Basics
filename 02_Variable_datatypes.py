#%%
# Shift-Enter: run cell select below
# Ctrl-Enter: run selected cells
# Alt+ Enter: run cell and insert below
# Tab: Code completion or ident
# Shift-Tab: Tooltip
# Matplotlib plotting: %matplotlib inline
# Reference
# Matthes, Eric (2002). Python Crash Course, 3rd Edition: A Hands-On, Project-Based Introduction to Programming. No Starch Press. 

#%%
# Variables and Data Types

# Variables : Every variable is connected to a value, which is the information associated with that variable. 
# Below 
# Variable is "message",
# Value is "Hello Python World" 
# List of Key words that Python that received for Functions : https://www.programiz.com/python-programming/keyword-list

message = "Hello Python World!"
print(message)

# %%
message = "Hello Python Crash Course World"
print(message)

# %%
# String: A string is a series of characters. 
# Anything inside the quotes is considered as string in Python.
# Can use single or double quotes ' ' or " "

name = "ada lovelace"
print(name.title())
# %%
name = "ada lovelace"
print(name.upper())
print(name.lower())
# %%
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
# %%
full_name = "{} {}". format(first_name, last_name)
print(full_name)
# %%
# adding whitespace
print("Python")
print("\tPython")
# %%
print("language:\nPython\nc\nJavescript")
# %%
print("Languages:\n\tpython\n\tc\n\tJavascript")

# %%
# Stripping whitespace
favorite_language = "Python "
print(favorite_language)
print(favorite_language.rstrip())
# %%
# Avoiding Syntax Errors with Strings
message = "One of Python's strength is its diverse community"
print(message)
# %%
# Numbers
# Integers
# you can add (+), Subtract (-), multiple (*), and divide(/) integers in Python

# 3**3 = 9 (two multiple will perform the exponential function)
# %%

# Floats : Python calls any number with a decimal point a float. 
# %%
# Integers and Floats
# When you divide any two numbers, even if they are integers that results in a whole number, you'll always get a float. 
# %%
# underscores in Numbers

universe_age = 14_000_000_000
print(universe_age)

# %%
# Multiple Assignment

x, y, z = 0, 0, 0
print(x, y, z)
# %%
 # Constants

MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

# %%
