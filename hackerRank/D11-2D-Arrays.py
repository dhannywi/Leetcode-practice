"""
Given a 6 X 6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Example

In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

Input Format

There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array A.

Constraints
-9 <= A[i][j] <= 9
0 <= i,j <= 5

Output Format

Print the maximum hourglass sum in A.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4
"""

# python3 solution

import math
import os
import random
import re
import sys

def hourglass_max_sum(arr):
    # keeping in mind the constraint of `-9 <= arr[i][j] <= 9`
    # minimum possible value we can have is -63 (if all value in the hourglass turns out to be -9)
    highest = -63
    for row in range(len(arr)-2):
        for col in range(len(arr[1])-2):
            top_sum = arr[row][col] + arr[row][col+1] + arr[row][col+2]
            middle = arr[row+1][col+1]
            bottom_sum = arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            
            hourglass_sum = top_sum + middle + bottom_sum
            
            if hourglass_sum > highest:
                highest = hourglass_sum
    print(highest)

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    hourglass_max_sum(arr)
