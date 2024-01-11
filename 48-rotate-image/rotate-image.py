class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for r in range(len(matrix)):
        #     for c in range(r):
        #         matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        # for lst in matrix:
        #     lst.reverse()
        # matrix.reverse()
        # for r in range(len(matrix)):
        #     for c in range(r):
        #         matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        m_len = len(matrix)
        left = 0
        right = m_len - 1
        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1
        
        for r in range(m_len):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

                