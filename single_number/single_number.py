'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# using built-in is same as using set() logic but with a list()

# def single_number(arr):
#     # traverse through list
#     for i in arr: 
#         # if count of current value
#         if arr.count(i) == 1:
#             # return value
#             return i
# O(n^2)

def single_number(arr):
    s = set()
    for num in arr: # O(n)
        if num in s: # O(1)
            s.remove(num)   # O(1)
        else:
            s.add(num)  # O(1)
    #only element in set is odd-element-out
    return list(s)[0] # O(1) because will always have 1 element
# O (n)

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")