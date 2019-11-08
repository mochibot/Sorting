# Quicksort - not required for the assignment but just wanted to add it here for my own reference

# Basic idea: divide and conquer
# Select a pivot (usually the first or last element). Loop through list and move everything <= pivot to the left (particitioning the array around pivot).
# Pivot ends in the position that it retains in the final sorted order
# Continue sorting the left half and right half of the array independently (recursion)

# Pros/cons:
# Average runtime of O(n log(n)) - faster than merge sort 
# Best if we can split the input as evenly as possible (each subarray is of size n/2)
# Worst-case scenario runtime of O(n^2) - when the input is already/almost sorted

def partition(arr):         #partition the list around the pivot (set to first element in this case)
    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    return left, pivot, right 

def quick_sort(arr):
    if len(arr) > 1:
        left, pivot, right = partition(arr)
        return quick_sort(left) + [pivot] + quick_sort(right)
    else:
        return arr 


# Merge sort

# Basic idea: another divide and conquer algorithm
# Recursively split the list to list of single element, which is considered as sorted. 
# Merge pairs of sorted lists until only 1 array remains.

# Pros/cons:
# Average runtime of O(n log n) - divide the list in half with each recursive call, and overall depth is O(n)
# Space complexity is O(n) - takes a lot of space and may slow down operations for large data sets 
# Can be optimized by replacing the merge functions with in-place merge 

# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    num_elements = len( arrA ) + len( arrB )
    merged_arr = [0] * num_elements
    # TO-DO
    index = 0
    while len(arrA) or len(arrB):
        if len(arrA) and (not len(arrB) or (arrA[0] < arrB[0])):
            smallest = arrA[0]
            arrA.remove(smallest)            
        else:
            smallest = arrB[0]
            arrB.remove(smallest)

        merged_arr[index] = smallest
        index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        midpoint = len(arr) // 2
        return merge(merge_sort(arr[:midpoint]), merge_sort(arr[midpoint:]))


# STRETCH: implement an in-place merge sort algorithm
# Change the merge logic. Instead of having a scratch array, move the data around within the original array
# Worst case scenario of O(n^2) runtime - entire right side needs to be moved to the left side

def merge_in_place(arr, start, mid, end):
    # TO-DO
    left = start
    right = mid + 1
    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            left += 1
        else:
            temp = arr[right]
            index = right
            while index > left:
                arr[index] = arr[index - 1]
                index -= 1
            arr[left] = temp
            left += 1
            right += 1 
            mid += 1

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO
    if l >= r:
        return arr
    else:
        midpoint = (l + r) // 2

        merge_sort_in_place(arr, l, midpoint)
        merge_sort_in_place(arr, midpoint + 1, r)
        return merge_in_place(arr, l, midpoint, r)

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt

# Timsort is based on insertion sort and merge sort.
# Used in Java, Python, Android platform, GNU Octave
# Basic idea - First sort small pieces using insertion sort, then merge the pieces using merge sort.
# I was unable to implement timsort on my own. This is what I pulled together from multiple sites on timsort.

def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        temp = arr[i]
        j = i

        while j > start and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = temp
    
    return arr

minrun = 32

def timsort( arr ):
    num = len(arr)

    for i in range(0, num, minrun):
        end = min(i + minrun - 1, num - 1)
        arr = insertion_sort(arr, i, end)
    
    curr_size = minrun
    while curr_size < num:
        for i in range(0, num, curr_size * 2):
            mid = min(num - 1, i + curr_size - 1)
            end = min(num - 1, mid + curr_size)
            arr = merge_in_place(arr, i, mid, end)
        curr_size *= 2

    return arr

print(timsort([2, 3, 1, 5, 7, 6, 0, -8, 240]))