class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Overall time: O(n log n), space: O(n)
        win = {}
        lose = {}
        for w, l in matches: # time: O(n)
            win[w] = win.get(w, 0) + 1
            lose[l] = lose.get(l, 0) + 1

        lost_0 = []
        lost_1 = []
        # lost 1 time
        for key, val in lose.items(): # time: O(n)
            if val == 1:
                lost_1.append(key)
        # won at least once, and never lost
        for key in win.keys(): # time: O(n)
            if key not in lose:
                lost_0.append(key)

        return [sorted(lost_0), sorted(lost_1)]# time: O(n log n)