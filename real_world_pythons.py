# Objective:
# The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.

# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

# Problem Statement:
# Given the initial menu:

# restaurant_menu = {
#     "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
#     "Main Course": {"Steak": 15.99, "Salmon": 13.99},
#     "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
# }
# Add a new category called "Beverages" with at least two items.
# Update the price of "Steak" to 17.99.
# Remove "Bruschetta" from "Starters".


# Add a new category called "Beverages" with at least two items.
# def steakhouse() :
    
restaurant_menu = {
        "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
        "Main Course": {"Steak": 15.99, "Salmon": 13.99},
        "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
restaurant_menu["beverages"] = "sodas", "alcohol" 
print(restaurant_menu)  

restaurant_menu = {
        "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
        "Main Course": {"Steak": 15.99, "Salmon": 13.99},
        "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
restaurant_menu["beverages"] = "sodas", "alcohol" 
restaurant_menu.update({"sodas":  "2.99"})
restaurant_menu.update({"alcohol": "5.99 and up!"})
print(restaurant_menu)


# Update the price of "Steak" to 17.99.


restaurant_menu["Main Course"].update({"Steak" :"17.99"})
print(restaurant_menu)


# Remove "Bruschetta" from "Starters".

del(restaurant_menu["Starters"]["Bruschetta"])
print(restaurant_menu)
