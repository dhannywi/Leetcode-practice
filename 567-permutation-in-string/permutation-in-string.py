class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window size 
        w = len(s1)
        # store char count of s1 & count of s2 char in 1st window
        pS1 = Counter(s1)
        pS2 = Counter(s2[0:w])

        # check 1st window permutation
        if pS2 == pS1:
            return True

        for i in range(w, len(s2)):
            # Update window by removing the leftmost character and adding the new character
            lc = s2[i - w]
            pS2[lc] -= 1
            if pS2[lc] == 0:
                del pS2[lc]
            pS2[s2[i]] += 1

            # check current window permutation
            if pS2 == pS1:
                return True

        return False