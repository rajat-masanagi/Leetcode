class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def axci(rectangles,axis):
            rectangles.sort(key=lambda x:x[axis])
            cuts,prev=0,-1

            for i in rectangles:
                start,end=i[axis],i[axis+2]
                if start>=prev:
                    cuts+=1
                prev=max(prev,end)
                if cuts>=3:
                    return True
            return False
        return axci(rectangles,0) or axci(rectangles,1)