'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    '''
    https://github.com/jacobpad/cs-module-project-iterative-sorting/blob/master/src/iterative_sorting/iterative_sorting.py
    '''




    for i in range(len(arr) - 1):       # Establish the length of the list
        cur_index = i                   # Set the 0 index to a variable
        for j in range(i+1, len(arr)):  #
            if arr[j] != 0:             # Sort the list smallest to largest, with '0' at the end, 
                                        # (skipping 0 with the `!=`)
                cur_index = j           # It becomes the current index
                                        #
        temp = arr[i]                   # This
        arr[i] = arr[cur_index]         # Is The
        arr[cur_index] = temp           # Swap

    return arr















if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    print('\n------------------')
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print('------------------\n')