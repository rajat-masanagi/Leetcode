class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q=[]
        for i in range(len(deck)):
            q.append(i)
        st=sorted(deck)
        ans=[0]*len(deck)
        for i in range(len(deck)-1):
            ans[q.pop(0)]=st[i]
            s=q.pop(0)
            q.append(s)
        ans[q[0]]=st[-1]
        return ans