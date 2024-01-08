"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer inputArray

An array of integers containing at least two elements.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 10,
-1000 ≤ inputArray[i] ≤ 1000.

[output] integer

The largest product of adjacent elements.
"""
def solution(inputArray):
    max_prod = -1000000 # max product of lower and upper bound
    # use sliding window and calculate product of two elements
    for i in range(len(inputArray)-1):
        prod = inputArray[i] * inputArray[i+1]
        if prod > max_prod:
            max_prod = prod
    return max_prod

# def solution(inputArray):
#     return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])
