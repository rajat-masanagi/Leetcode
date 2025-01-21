class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        for i in range(len(boxes)):
            sum=0
            for j in range(len(boxes)):
                sum+=abs(i-j)*int(boxes[j])
            ans.append(sum)
        return ans