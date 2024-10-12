class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        tv=0
        fv=0
        sv=0
        n=len(grid)
        for i in range(n):
            maxi=0
            maxj=0
            for j in range(n):
                if grid[i][j]>maxi:
                    maxi=grid[i][j]
                if grid[j][i]>maxj:
                    maxj=grid[j][i]
                if grid[i][j]>0:
                    tv+=1
            sv+=maxj
            fv+=maxi
        return fv+sv+tv
