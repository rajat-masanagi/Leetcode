class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        yset=set()
        xset=set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    yset.add(j)
                    xset.add(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in xset or j in yset:
                    matrix[i][j]=0