# Recursive Selection Sort Algorithm in Python 3 

import random
import time


def largeIndex(array, first, last):
    # TODO: find the index of largest element in given range
    if first == last:
        return first
    else:
        index = largeIndex(array, first + 1, last)
        if array[first] > array[index]:
            return first
        else:
            return index


def recursive_selection_sort(array, array_len, index = 0): 
    # TODO: sort the given array with selection sort
    # index: the starting index
    
    # if the index becomes the largest possible index, return the array
    # base case
    if index == array_len - 1 or array_len == 0:
        return
    # if it is not base case
    else:
        # find the index of largest element
        large_index = largeIndex(array, index, array_len - 1)
        if large_index != index:
            # swapping
            temp = array[index] 
            array[index] = array[large_index]
            array[large_index] = temp            
        # recursion, call the function by adding 1 to starting index
        recursive_selection_sort(array, array_len, index + 1)


def iterative_selection_sort(data):

    for index in range(len(data)):
        large_index = index
        
        # finding largest
        for i in range(index,len(data)):
            if data[i] > data[large_index]:
                large_index = i
        
        # swapping
        temp = data[index] 
        data[index] = data[large_index]
        data[large_index] = temp
    
    return data
    

if  __name__== "__main__":
    # Define the list of random numbers
    array_1 = [random.randint(1,1000) for i in range(200)]
    array_2 = array_1[:]
    array_len = len(array_1)
    sorted_list = sorted(array_1, reverse=True)
      
    # Calculate the execution time
    start_rec = time.time()
    recursive_selection_sort(array_1, array_len)
    end_rec = time.time()
    
    start_iter = time.time()
    iterative_selection_sort(array_2)
    end_iter = time.time()
    
    # Print the rsults
    print('The execution time:')
    print(' - Recursive selection sort: {}'.format(end_rec - start_rec))
    print(' - Iterative selection sort: {}'.format(end_iter - start_iter))
