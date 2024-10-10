items = ["apple", "banana", "orange", "mango", "apple"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate", item)
        break
    unique_item.add(item)
