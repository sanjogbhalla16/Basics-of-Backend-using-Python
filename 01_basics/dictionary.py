# these use curly braces for representation

chai_types = {"Masala": "Spicy", "Lemon": "zesty", "Green": "Fresh"}

# print(chai_types)

chai_types["Masala1"] = "Spicy1"

# print(chai_types)

del chai_types["Green"]

# print(chai_types)


# nested dictionary

tea_shop = {
    "chai": {"Masala": "Spicy", "Lemon": "zesty", "Green": "Fresh"},
    "Tea": {"Green": "Mild", "Black": "strong"},
}

print(tea_shop)


squared_numbers = {x: x**2 for x in range(6)}

print(squared_numbers)
