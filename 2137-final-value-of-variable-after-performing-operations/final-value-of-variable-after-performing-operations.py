class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        r=0
        for i in operations:
            if i[0]=='-' or i[-1]=='-':
                r=r-1
            elif i[0]=='+' or i[-1]=='+':
                r=r+1
        return r