class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d=[0]*k
        for i in arr:
            d[(i%k+k)%k]+=1
        
        if d[0]%2!=0:
            return False
        
        for i in range(1,k//2+1):
            if d[i]!=d[k-i]:
                return False
        return True