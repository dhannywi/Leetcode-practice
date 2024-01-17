class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        lost = {}
        for i in range(len(matches)):
            win[matches[i][0]] = win.get(matches[i][0], 0) + 1
            lost[matches[i][1]] = lost.get(matches[i][1], 0) + 1

        winners = []
        lost_1 = []
            
        for k, v in lost.items():
            if v == 1:
                lost_1.append(k)
        for k in win.keys():
            if k not in lost:
                winners.append(k)

        winners.sort()
        lost_1.sort()
        return [winners, lost_1]
        # return [[p have never lost], [p lost 1 match]]