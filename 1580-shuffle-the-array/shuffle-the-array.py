class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        pt1=0
        pt2=n
        for i in range(2*n):
            if(i%2==0):
                ans.append(nums[pt1])
                pt1+=1
            else:
                ans.append(nums[pt2])
                pt2+=1
        return ans
