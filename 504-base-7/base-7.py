class Solution:
    def convertToBase7(self, num: int) -> str:
        s=''
        temp=abs(num)
        while temp!=0:
            s=str(temp%7)+s
            temp=temp//7
        if num<0:
            return '-'+s
        elif num==0:
            return '0'
        else:
            return s