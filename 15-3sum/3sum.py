class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        pos=set()
        neg=set()
        zerocount=0
        po=0
        ne=0
        parr=[]
        narr=[]
        for i in range(n):
            if nums[i]>0:
                pos.add(nums[i])
                parr.append(nums[i])
                po+=1
            elif nums[i]<0:
                neg.add(nums[i])
                narr.append(nums[i])
                ne+=1
            else:
                zerocount+=1
        
        ans=set()
        if zerocount>=3:
            ans.add((0,0,0))
        if zerocount>=1:
            for i in pos:
                complement = - i
                if complement in neg:
                    ans.add((-i,0,i))
        for i in range(ne):
            for j in range(i+1,ne):
                complement = - narr[i] - narr[j]
                if complement in pos:
                    ans.add(tuple(sorted([narr[i],narr[j],complement])))
        
        for i in range(po):
            for j in range(i+1,po):
                complement = - parr[i] - parr[j]
                if complement in neg:
                    ans.add(tuple(sorted([parr[i],parr[j],complement])))
             
        return list(ans)

