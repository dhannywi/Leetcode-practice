class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # store char count of s1
        pS1 = Counter(s1)
        # window size and right pointer
        w = r = len(s1)
        for i in range(len(s2) - w+1): # O(n+w)
            # store char count of s2 current window
            pS2 = Counter(s2[i:r])
            if pS2 == pS1:
                return True
            else:
                r += 1
        return False

        