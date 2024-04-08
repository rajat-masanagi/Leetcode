class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        sol=[]
        for i in range(len(number)):
            if(number[i]==digit):
                sol.append(number[:i]+number[i+1:])
        return max(sol)
