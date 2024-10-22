# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        q=deque([root])
        while q:
            n=len(q)
            ls=0
            for i in range(n):
                node =q.popleft()
                ls+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(ls)
        if k>len(res):
            return -1
        res.sort(reverse=True)
        return res[k-1]