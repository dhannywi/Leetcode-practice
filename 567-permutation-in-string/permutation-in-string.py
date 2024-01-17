class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # store char count of s1
        pS1 = {}
        for i in s1:
            pS1[i] = pS1.get(i, 0) + 1
        # window size
        w = len(s1)
        # store char count of s2 in a window
        pS2 = Counter()
        r = w
        for i in range(len(s2)- w+1):
            pS2 = Counter(s2[i:r])
            if pS2 == pS1:
                return True
            else:
                del pS2
                r += 1
        return False

        