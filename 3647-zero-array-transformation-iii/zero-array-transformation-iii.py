class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        total=0
        r=0
        heap=[]
        arr=[0]*(len(nums)+1)
        for i,num in enumerate(nums):
            total+=arr[i]
            while r<len(queries) and queries[r][0] == i:
                heapq.heappush(heap,-queries[r][1])
                r+=1
            while total<num:
                if not heap or -heap[0]<i:
                    return -1
                arr[1-heapq.heappop(heap)]-=1
                total+=1
        return len(heap)