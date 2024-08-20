nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Is 5 in the nested list?", any(5 in sublist for sublist in nested_list))
print("Is 10 in the nested list?", any(10 in sublist for sublist in nested_list)) 
print("Is 3 not in the nested list?", all(3 not in sublist for sublist in nested_list)) 
print("Is 8 in the nested list?", any(8 in sublist for sublist in nested_list)) 
