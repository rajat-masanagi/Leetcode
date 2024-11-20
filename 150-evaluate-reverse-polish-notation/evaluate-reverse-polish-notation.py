import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=='+':
                val2=stack.pop()
                val1=stack.pop()
                stack.append(val1+val2)
            elif i=='-':
                val2=stack.pop()
                val1=stack.pop()
                stack.append(val1-val2)
            elif i=='*':
                val2=stack.pop()
                val1=stack.pop()
                stack.append(val1*val2)
            elif i=='/':
                val2=stack.pop()
                val1=stack.pop()
                ans=val1/val2
                if ans<0:
                    stack.append(math.ceil(ans))
                else:
                    stack.append(math.floor(ans))
            else:
                stack.append(int(i))
        return stack[0]
