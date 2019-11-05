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
def merge_in_place(arr, start, mid, end):
    # TO-DO
    
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
