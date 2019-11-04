# TO-DO: Complete the insertion_sort() function below 

# Basic idea:
# Split collection into sorted and unsorted sections. First element is automatically in sorted section. 
# Loop through list starting with index 1. Compare with everything in sorted section. Shift the element until it reaches correct position.

# Pros/cons:
# Runtime depends on how close to being in-order the data is to begin with. O(n) in the best-case scenario. Slow for big data sets.
# O(n^2) runtime in the worst-case scenario (each element is compared with all the other elements in the sorted array, so n * n comparisons).
# Sorting can be done in place, requiring O(1) space

def insertion_sort( arr ):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i

        while j > 0 and temp < j - 1:     # shift element until it is in correct position
            arr[j] = arr[j - 1]
            j -= 1
        
        arr[j] = temp                     # insert element

    return arr


# TO-DO: Complete the selection_sort() function below 

# Basic idea: 
# Repeatedly find the min element from the unsorted part of the array and put it in its correct position in an sorted part of the array

# Pros/cons: 
# Runtime of O(n^2), even if input is already sorted. Impractical to use with large data sets.
# Only requires a constant amount of space (O(1)).

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):        # find the smallest element in the part of the array to the right of the current index
            if arr[j] < arr[smallest_index]:
                smallest_index = j     

        # TO-DO: swap
        temp = arr[i]                          
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below

# Basic idea: 
# Loop through list and repeatedly compare pairs of adjacent elements, swapping their positions if they exist in the wrong order. Continue looping until no swap is made.

# Pros/cons:
# O(n) runtime in the best-case scenario (if the input array is already sorted)
# O(n^2) runtime in the worst-case scenario (n passes through the data, each pass testing n-1 pairs). Highly inefficient for larget data sets. 
# Good for testing whether the list is sorted (give best-case running time of O(n)). Require very little memory other than that which the list itself occupies.

def bubble_sort( arr ):
    swapped = True
    while swapped:          # stop looping once no swap is made
        swapped = False 
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapped = True
    
    return arr

# STRETCH: implement the Count Sort function below

# Basic idea: 
# Loop through the array, count the # of times each item occurs. Use the count to compute an item's index in the final sorted array.

# Pros/cons:
# O(n) runtime, making it faster than comparison-based algorithms
# Input is restricted (only works when the range is known ahead of tme)
# O(n) space cost (require a lot of space for wide-ranged values)

def count_sort( arr, maximum=-1 ):
    if any(val < 0 for val in arr):
        return 'Error, negative numbers not allowed in Count Sort'

    arr_max = max(arr or [0])

    counts = []
    for i in range(0, arr_max + 1):
        counts.append(0)
    
    for val in arr:
        counts[val] += 1

    index = 0

    for i in range(0, len(counts)):    
        while counts[i] > 0:
            arr[index] = i
            index += 1
            counts[i] -= 1
    
    return arr