class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = len(grid)
        s = l ** 2
        m = {}
        a = 0
        b = 0

        for i in range(s):
            m[i + 1] = 0
        
        for i in range(l):
                for j in range(l):
                    if (i < l):
                        m[grid[i][j]] += 1
        for k, v in m.items():
            if (v > 1):
                a = k

            if (v == 0):
                b = k
            
        return [a, b]