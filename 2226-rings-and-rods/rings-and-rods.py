class Solution:
    def countPoints(self, rings: str) -> int:
        d={"0":{""},"1":{""},"2":{""},"3":{""},"4":{""},"5":{""},"6":{""},"7":{""},"8":{""},"9":{""}}
        flag=0
        for i in range(1,len(rings),2):
            print(rings[i])
            d[rings[i]].add(rings[i-1])
        for i in list(d.keys()):
            if(len(d[i])==4):
                flag+=1
        return flag
                
        

