class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxArea=0
        for i in range(len(heights)):
            start=i
            while stack and stack[-1][1] >heights[i]:
                start,h=stack.pop()
                maxArea=max(maxArea,(i-start)*h)
            stack.append([start,heights[i]])
        n=len(heights)
        while stack:
            maxArea=max(maxArea,(n-stack[-1][0])*stack[-1][1])
            stack.pop()
        return maxArea