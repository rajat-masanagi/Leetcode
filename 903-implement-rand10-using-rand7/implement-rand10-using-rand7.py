# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        t=0
        for i in range(5):
            t+=rand7()
        return (t)%10+1
        