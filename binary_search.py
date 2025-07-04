def binary_serach (list,target):
    first = 0
    last = len(list) - 1 #lenght of the list minus one as index starts from 0

    while first <= last:
        mid = (first + last) // 2 #floor division to find the middle index then rounded down
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in the list.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #in binary search the list must be sorted in ascending order

result = binary_serach(numbers, 12)
verify(result)

result = binary_serach(numbers, 6)
verify(result)
