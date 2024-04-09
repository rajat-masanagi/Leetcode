class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t=0
        m=tickets[k]
        for i in range(len(tickets)):
            if tickets[i]<m:
                t+=tickets[i]
            elif tickets[i]>=m and i<=k:
                t+=m
            elif tickets[i]>=m and i>k:
                t+=m-1
        return t