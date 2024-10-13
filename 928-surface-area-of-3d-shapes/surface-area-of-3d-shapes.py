class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area=0
        n=len(grid)
        if n==1:
            if grid[0][0]==0:
                return 0
            else:
                return grid[0][0]*4+2
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1:
                    area+=grid[i][j]
                if j==0 or j==n-1:
                    area+=grid[i][j]
                if i+1<n:
                    area+=abs(grid[i][j]-grid[i+1][j])
                if j+1<n:
                    area+=abs(grid[i][j]-grid[i][j+1])
                if grid[i][j]:
                    area+=2

        return area