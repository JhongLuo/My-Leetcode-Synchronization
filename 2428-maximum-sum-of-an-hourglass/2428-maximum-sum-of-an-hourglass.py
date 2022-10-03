from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                prefix_sum[i + 1][j + 1] = (
                    prefix_sum[i + 1][j]
                    + prefix_sum[i][j + 1]
                    - prefix_sum[i][j]
                    + grid[i][j]
                )
        res = 0
        for i in range(n - 2):
            for j in range(m - 2):
                summa = (
                    prefix_sum[i + 3][j + 3]
                    - prefix_sum[i][j + 3]
                    - prefix_sum[i + 3][j]
                    + prefix_sum[i][j]
                    - grid[i + 1][j]
                    - grid[i + 1][j + 2]
                )
                # print(summa, grid[i + 1][j], grid[i + 1][j + 2])
                res = max(res, summa)
        return res
