class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # create array of string
        s_arr = [i for i in s]
        # traverse the s_arr, adding only non-vowel to a new string
        new_str = ''
        for i in s_arr:
            if i not in vowels:
                new_str += i
        return new_str