class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use only alphanumeric chars in string O(n)
        # s_alnum = ''
        # for c in s:
        #     if c.isalnum():
        #         s_alnum += c.lower()
        # two pointer approach
        # left = 0
        # right = len(s_alnum) - 1
        # while left < right:
        #     if s_alnum[left] != s_alnum[right]:
        #         return False
        #     else:
        #         left += 1
        #         right -= 1
        # return True

        s_alnum = [i.lower() for i in s if i.isalnum()]
        return s_alnum == s_alnum[::-1]
