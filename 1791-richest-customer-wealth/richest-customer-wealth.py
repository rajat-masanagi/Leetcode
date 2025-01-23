class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for i in accounts:
            bal=0
            for j in i:
                bal+=j
            if bal>maxi:
                maxi=bal
        return maxi
