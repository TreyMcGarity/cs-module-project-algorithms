'''
Input: an integer
Returns: an integer
'''
# def eating_cookies(n):
# runtime complexity = O(3^n) because of 3 ways to eat raised by number of cookies
#     # n 0 or less
#     if n <= 0:
#         # 1 way to eat
#         return 1
#     # n is 1 or 2
#     elif n < 3:
#         # n ways to eat
#         return n
#     else:
#         # each recall represents a branch of possibilities
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

def eating_cookies(n , cache=None):
# runtime complexity = O(n) because cache storing previous solutions
    if not cache:
        cache = [0 for _ in range(n+1)]
    if n <= 0:
        return 1
    if n < 3:
        return n
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
