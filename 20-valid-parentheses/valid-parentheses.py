class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(': ')', '{': '}', '[': ']'}
        stack = []


        for e in s:
            if e in valid:
                stack.append(e)
            else:
                if not stack:
                    return False
                previous = stack.pop()
                if valid[previous] != e:
                    return False
        return not stack

