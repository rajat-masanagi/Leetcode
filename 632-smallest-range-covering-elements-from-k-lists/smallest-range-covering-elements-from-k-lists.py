import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap=[]
        curr_max=-10e5
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i][0],i,0))
            curr_max=max(curr_max,nums[i][0])
        rs=-10e5
        re=10e5
        while heap:
            mini,li,idx=heapq.heappop(heap)
            if curr_max-mini<re - rs:
                rs,re=mini,curr_max
            if idx + 1 < len(nums[li]):
                next_element=nums[li][idx+1]
                heapq.heappush(heap,(next_element,li,idx+1))
                curr_max=max(curr_max,next_element)
            else:
                break
        return [rs,re]