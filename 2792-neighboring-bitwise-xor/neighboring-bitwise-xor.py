class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        count=0
        for i in derived:
            if i==1:
                count+=1
        if count%2==0:
            return True
        else:
            return False