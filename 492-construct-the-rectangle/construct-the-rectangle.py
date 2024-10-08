class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        divs=[]
        for i in range(1,area):
            if area%i==0:
                if i>area//i:          
                    divs.append([i,area//i])
                else:
                    divs.append([area//i,i])
        min_diff=area
        min_index=0
        for i in range(len(divs)):
            if abs(divs[i][0]-divs[i][1])<min_diff:
                min_diff=abs(divs[i][0]-divs[i][1])
                min_index=i
        if area==1:
            return [1,1]
        return divs[min_index]