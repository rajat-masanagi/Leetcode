class Solution:
    def minPartitions(self, n: str) -> int:
        max="0"
        for i in n:
            if i>max:
                max=i
        return int(max)