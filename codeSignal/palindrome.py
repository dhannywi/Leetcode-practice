"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.
"""
def solution(inputString):
    # returns true if inputString is a palindrome, false otherwise.
    reverse_str = inputString[::-1]
    if inputString == reverse_str:
        return True
    else:
        return False

# def solution(inputString):
#     return inputString == inputString[::-1]
