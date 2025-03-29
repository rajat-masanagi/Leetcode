class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        if numRows==1:
            return ans
        prev_rows=self.generate(numRows-1)
        prev_row=prev_rows[-1]
        curr=[1]
        for i in range(1,numRows-1):
            curr.append(prev_row[i-1]+prev_row[i])
        curr.append(1)
        prev_rows.append(curr)
        return prev_rows

        