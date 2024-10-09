import math
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area=0
        for i in range(len(points)):
            for j in range(1,len(points)):
                for k in range(2,len(points)):
                    a=math.sqrt((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)
                    b=math.sqrt((points[i][0]-points[k][0])**2+(points[i][1]-points[k][1])**2)
                    c=math.sqrt((points[k][0]-points[j][0])**2+(points[k][1]-points[j][1])**2)
                    s=(a+b+c)/2
                    area=math.sqrt(abs(s*(s-a)*(s-b)*(s-c)))
                    if area>max_area:
                        max_area=area

        return max_area