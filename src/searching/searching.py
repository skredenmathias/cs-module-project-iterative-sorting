def linear_search(arr, target):
    # Your code here
    # search array 1 by 1 until target is found / arr ends
    for i in range(len(arr)): # (1, len(arr)) #?
        if target == arr[i]:
            return True

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Set boundaries for low and high marks to search
    low = 0
    high = len(arr)
    # while low and high do not overlap:
    while low < high:
        # check the midpoint
        mid = (low + high) // 2
        # if it's equal, return True
        if arr[mid] == target:
            return True
        # Else, if target is smaller, set array to left half and repeat
        elif target < arr[mid]
            #set high to midpoint value
            high = mid # -1 #?
        # Else, if target is larger, set array to right half and repeat
        else:
            # set the low to midpoint value
            low = mid + 1
    # if we get to the end, return False
    return -1  # not found

# recursive solution?