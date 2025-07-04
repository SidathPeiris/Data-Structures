def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = len(list) // 2 #floor division to find the middle index then rounded down
        
        if list[mid] == target:
            return True
        elif list[mid] < target:
            return recursive_binary_search(list[mid + 1:], target) #create a new sublist with elements after the middle index till end of list
        else:
            return recursive_binary_search(list[:mid], target) #create a new sublist with elements from the beginning of the list till the middle index

"""
Have to use a return function to return the result of the recursive call, as you have to use the result of the recursive call to determine if the target is found in the sublist.
"""

def verify(result):
    print("Target found:", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = result = recursive_binary_search(numbers, 6)
verify(result)
