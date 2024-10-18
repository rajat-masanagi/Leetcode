import heapq
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        h=nums
        heapify(h)
        for i in range(len(h)//2):
            alice=heappop(h)
            bob=heappop(h)
            arr.append(bob)
            arr.append(alice)
        return arr