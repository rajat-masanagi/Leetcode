import math
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        l1=math.sqrt((points[0][0]-points[1][0])**2+(points[0][1]-points[1][1])**2)
        l2=math.sqrt((points[0][0]-points[2][0])**2+(points[0][1]-points[2][1])**2)
        l3=math.sqrt((points[2][0]-points[1][0])**2+(points[2][1]-points[1][1])**2)
        if round(l1+l2,5)==round(l3,5) or round(l2+l3,5)==round(l1,5) or round(l1+l3,5)==round(l2,5):
            return False
        else:
            return True