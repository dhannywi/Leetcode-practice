class Solution:
    def is_palindrome(self, l, r, s):
        # check if string is palindrome
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.is_palindrome(l+1, r, s) or self.is_palindrome(l, r-1, s)
            l += 1
            r -= 1
        
        return True

# "aba"
# a==a