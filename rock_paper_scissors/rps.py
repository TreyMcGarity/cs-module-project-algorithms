#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  """
  need to save choices and output
  make a function to recall at new n
  """
  # choices and output arrays
  choices=['rock', 'paper', 'scissors'] 
  output=[]
  # function to take num of plays and array of possible set
  def make_set(n, possible_set):
    # if num of plays is 0
    if n == 0:
      # add set of possibilities to output
      output.append(possible_set)
    else:
      # traverse through choices array
      for x in choices:
        # call function on n - 1
        # and add x to possible_set 
        make_set(n - 1, possible_set + [x])
  # initiate recall of function at initial num of plays and empty array
  make_set(n,[])
  return output
"""
$ py rps.py 2
current   | n | possible_set | added to poss_set
            2   []            
rock      | 1 | ['rock']     | ['rock'] 
paper     | 1 | ['rock']     | ['paper']
scissors  | 1 | ['rock']     | ['scissors']
rock      | 2 | []           | ['rock']
rock      | 1 | ['paper']    | ['rock']
paper     | 1 | ['paper']    | ['paper']
scissors  | 1 | ['paper']    | ['scissors']
paper     | 2 | []           | ['paper']
rock      | 1 | ['scissors'] | ['rock']
paper     | 1 | ['scissors'] | ['paper']
scissors  | 1 | ['scissors'] | ['scissors']
scissors  | 2 | []           | ['scissors']

output = [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], 
['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], 
['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
"""

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')