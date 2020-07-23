'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):

    total_product = list(range(len(arr)))       # Make a list the same length as `arr`

    def get_product(arr):
        ''' Get the product of the `arr` list '''
        result = 1
        for i in arr:
            result = result * i
        return result  

    prod = get_product(arr)                     # Call the above function

    for i in range(len(total_product)):         # Fill the list with the product in each index
        total_product[i] = prod


    lst = []                                    # Make a new list
    for i in range(len(total_product)):
        num = total_product[i] // arr[i]        # Devide each index of `total_product` by the index value at the corrosponding original `arr` index
        lst.append(num)                         # Put it all in a list again

    return lst                                  # Return it






if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 7, 3, 4]
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    print('\n------------------')
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    print('\n------------------')
