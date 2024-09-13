#%%
#Introducing List
    # What is a list?
    # Changing, Adding, Removing Elements
    # Organizing a List
    # Avoiding Index Errors When Working with Lists

# %%

# Types in Python
x = x = 5
s = "geeksforgeeks"
y = [1,2,3]
print(type(x))
print(type(s))
print(type(y))

# %%

# What is list? A list is a collection of items in particular order. 
# List could include letters of the alphabets, the digit from 0-9, or name of all the people in your family.
# Because multiple items are in a list, so keeping the names plural is a good practice

# Square bracket [] indicate a list
# individual element in a list is separated by commas. 

bicycles = ["trek", "cannodale", "redline", "specialized"]
print(bicycles)
#%%
#Accessing Elements in a List
#Accessing Elements in a list are ordered collections, so you can access any element in a list by telling python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index enclosed in square brackets. For Example, let's pull out the first bicycle in the list bicycles:
print(bicycles[0])
# You can also use the string methods in the list, you can format the element 'trek' more neatly by using the title ()method:

print(bicycles[0].title())





# %%
#Index Positions Start at 0, Not 1

#Python considers the first item in a list to be at position 0, not position 1. This is true of most programming languages, and the reason has to do with list operations are implemented at a lower level. If you're receiving unexpected results, determine where you are making a simple off-by-one error
print(bicycles[1])
print(bicycles[3])
# %%
# by asking for the item at index -1, python always returns the last item in the list
print(bicycles[-1])
# %%
#Using Individual Values from a List
# you can use f-string to create a message based on a value from a list. Let's try pulling the first bicycle from the list and composing a message using that value.

bicycles = ["trek", "cannondale", "redline", "specialized"]
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
# %%

# Adding, Changing, removing and Modifing elements

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# %%
# Modifying Element in a list
motorcycles[0] = "ducati"
print(motorcycles)
# %%

### Adding Elements to a List
motorcycles.append("ducati")
print(motorcycles)
# %%
motorcycles =[]
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)
# %%
motorcycles.insert(0,"ducati")
print(motorcycles)
# %%
print (motorcycles)
# %%
del motorcycles[0]
print(motorcycles)
# %%
del motorcycles[1]
print(motorcycles)
# %%
#Removing an item using the pop() Method
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
# %%
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
# %%
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# %%
motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(motorcycles)
# %%
# Removing an item by value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)


# %%
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
# %%

# Organizing a List 
# Sorting a List Permanently with the sort() Method

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
# %%
# You can also short the list in reverse alphabetical order by passing the argument reverse = True to sort()method
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)
# %%
# Sorting a List Temporarily with the sorted () Function
#using sorted() function

cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# %%
# Printing a list in Reverse Order 
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
cars.reverse()
print(cars)
# %%
#Finding the Length of a List using len()function
cars = ["bmw", "audi", "toyota", "subaru"]
len(cars)


# %%
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles[-1])
# %%
motorcycles = []
# print(motorcycles[-1])
# %%
