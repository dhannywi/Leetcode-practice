class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        
        pos_s = pos_t = 0
        found = []
        while pos_s < len(s) and pos_t < len(t):
            if s[pos_s] != t[pos_t]:
                pos_t += 1
            else:
                found.append(True)
                pos_s += 1
                pos_t += 1
        
        if len(found) == len(s):
            return True
        return False
        
