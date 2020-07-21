def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)): 

        if arr[i] == target: 
            return i 


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = len(arr) - 1
    while   start <= end:
        midindex = (end + start) // 2
        if target == arr[midindex]:
            return midindex
        if target < arr[midindex]:
            end = midindex - 1
        if target > arr[midindex]:
            start = midindex + 1

    return -1  # not found
