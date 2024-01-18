class Solution: # solution using one dictionary | time: O(m+n) | space: O(m)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # store count of magizine character
        mg = {}
        for e in magazine:
            mg[e] = mg.get(e, 0) + 1
  
        # decrease count in mg if used for ransome note
        for i in ransomNote:
            if i not in mg or mg[i] == 0:
                return False
            else:
                mg[i] -= 1
        return True