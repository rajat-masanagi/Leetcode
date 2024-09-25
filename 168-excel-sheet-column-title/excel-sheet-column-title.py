class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        t=''
        temp=columnNumber
        while temp!=0:
            e=temp%26
            if e==0:            # If character is Z subtract 1
                t='Z'+t         # Eg 52//26 =2 so (52-1)//2 =1
                temp=temp-1     
            else:
                t=chr(e+64)+t
            temp=temp//26
        return t
