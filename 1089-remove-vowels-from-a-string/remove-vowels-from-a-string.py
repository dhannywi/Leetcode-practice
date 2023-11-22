class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # traverse the s_arr, adding only non-vowel to a new string
        for vowel in vowels:
            s = s.replace(vowel, '')
        return s