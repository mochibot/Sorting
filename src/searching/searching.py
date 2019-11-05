# STRETCH: implement Linear Search
# O(n) runtime - loop over the array once
 				
def linear_search(arr, target):
  
    # TO-DO: add missing code
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
# Precondition: data is already sorted either alphabetically or numerically
# O(log(n)) runtime - think about how many times can you divide N by 2 until you have 1 (log 2 N)

def binary_search(arr, target):

    if len(arr) == 0:
        return -1 # array empty

    low = 0                 # set boundary of sort
    high = len(arr)-1

    # TO-DO: add missing code

    while high >= low:
        middle = (low + high) // 2     # // is ~ to Math.floor()

        if target == arr[middle]:      # if target is same as midpoint, we are done
            return middle
        elif target < arr[middle]:     
            high = middle - 1          # narrow down to left side of the array
        else:
            low = middle + 1           # narrow down to right side of the array

    return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
    middle = (low + high) // 2

    if len(arr) == 0:
        return -1 # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if target == arr[middle]:
        return middle
    elif target < arr[middle]:
        return binary_search_recursive(arr, target, low, middle - 1)
    else:
        return binary_search_recursive(arr, target, middle + 1, high)