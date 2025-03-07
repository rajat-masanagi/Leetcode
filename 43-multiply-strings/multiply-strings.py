class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        n2=0
        x=0
        for i in num1[::-1]:
            n1+=int(i)*(10**x)
            x+=1
        x=0
        for i in num2[::-1]:
            n2+=int(i)*(10**x)
            x+=1
        print(n1,n2)
        return str(n1*n2)
        