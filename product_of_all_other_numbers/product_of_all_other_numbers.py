'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
# runtime complexity = O(2n) because manipulating array twice
    #temporary variable for the multiples
    temp = 1
    # initialize a array of 1's same size as input array
    products = [1 for i in range(len(arr))] 
    # traverse through excluding arr[i]  
    for i in range(len(arr)):
        # set current value in product array position to temp
        products[i] = temp 
        # multiply temp by current value in input array position
        temp *= arr[i]
    #reset temp to 1
    temp = 1
    # traverse backwards excluding arr[i]
    for i in range(len(arr)-1, -1, -1):
        # multiple current value in product array by temp
        products[i] *= temp 
        # then multiply temp by current value in input array
        temp *= arr[i]

    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
