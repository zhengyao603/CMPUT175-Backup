def binarySearch (listNumbers, low, high, key):
    # find the mid index of the current subarray
    mid_index = (low + high) // 2
    # return the index if it matches with the mid element of the list
    if key == listNumbers[mid_index]:
        return mid_index
    else:
        # return -1 if the key is not in the list
        if high == low:
            return -1
        else:
            if key > listNumbers[mid_index]:
                return binarySearch(listNumbers, mid_index + 1, high, key)
            elif key < listNumbers[mid_index]:
                return binarySearch(listNumbers, low, mid_index - 1, key)


# Test array 
def main():
    array_for_test = [-8,-2,1,3,5,7,9]
    print(binarySearch(array_for_test, 0, len(array_for_test)-1, 9))
    print(binarySearch(array_for_test, 0, len(array_for_test)-1, -8))
    print(binarySearch(array_for_test, 0, len(array_for_test)-1, 4))
    
main()