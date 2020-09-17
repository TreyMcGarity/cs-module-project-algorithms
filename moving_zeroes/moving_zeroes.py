'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    output = []
    # traverse through list
    for i in arr:
        # if current value is 0
        if i == 0:
            # add zero to end of list
            output.append(i)
        else:
            # add non-zero to beginning
            output.insert(0, i)
    return output

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")