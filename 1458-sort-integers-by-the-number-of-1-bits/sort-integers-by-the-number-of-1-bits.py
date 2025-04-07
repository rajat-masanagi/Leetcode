class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def numberofones(decimal):
            count=0
            while decimal!=0:
                if decimal%2==1:
                 count+=1
                decimal=decimal//2
            return count
        d=[]
        for i in arr:
            d.append([i,numberofones(i)])
        sorted_d = sorted(d, key=lambda k: (k[1],k[0]))
        ans = [x[0] for x in sorted_d]
        return ans