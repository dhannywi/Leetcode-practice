class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # store counts of char in string
        c_count = {}
        for i in sentence:
            c_count[i] = c_count.get(i, 0) +1
        # see chars in c_count
        chars = [i for i in c_count.keys()]

        # english alphabets = 26
        return len(chars) == 26