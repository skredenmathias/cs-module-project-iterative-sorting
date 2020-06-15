# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        # temp = arr[i]
        # arr[i] = arr[smallest_index]
        # arr[smallest_index] = temp

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    # Compare the first and second item of a collection. If the first item is bigger than the second item, swap the items.

    # Move to the next item. Now, we will compare the second item with the third item. If the second item is bigger than the third, swap the items.

    # Do this for every item until the end of the list.

    # Repeat steps 1-3 (decrementing “the end of the list” by 1 each time).
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
