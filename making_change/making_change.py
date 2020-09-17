#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # 0 cents, only 1 way to get change, and is a valid solution
  if amount == 0:
    return 1
  # if there is a negative number
  elif amount < 0:
    return 0
  # no coins left but there is a positive amount of cents needed: return 0 ways
  elif len(denominations) == 0:
    return 0
  largest_coin = denominations[-1]
  # recall with the largest coin used plus recall with the largest coin used
  # first: when runs through, if amount minus largest coin gives zero returns 0 also
  #   if it returns a positive value runs again and same check until reaches negative
  # second: takes off largests coin value to keep narrowing until no denominations
  return making_change(amount - largest_coin, denominations) + making_change(amount, denominations[:-1])

"""
10 [1, 5, 10, 25, 50]   ORIGINAL
-40 [1, 5, 10, 25, 50]
10 [1, 5, 10, 25]
-15 [1, 5, 10, 25]
10 [1, 5, 10]
0 [1, 5, 10]    MEANS 1 DIME WORKS
10 [1, 5]
5 [1, 5]        ONE NICKEL LEAVES POS VALUE SO
0 [1, 5]        MEANS 2 NICKELS WORKS
5 [1]           BUT ALSO
4 [1]
3 [1]
2 [1]
1 [1]
0 [1]           MEANS 1 NICKEL W/ 5 PENNIES WORKS
1 []
2 []
3 []
4 []
5 []
10 [1]
9 [1]
8 [1]
7 [1]
6 [1]
5 [1]
4 [1]
3 [1]
2 [1]
1 [1]
0 [1]           MEANS 10 PENNIES WORKS
1 []
2 []
3 []
4 []
5 []
6 []
7 []
8 []
9 []
10 []
There are 4 ways to make 10 cents.
"""
if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")