list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6]

missing_elements = [item for item in list1 if item not in list2]
print("Missing elements from list2:", missing_elements)
