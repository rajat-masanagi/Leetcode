# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x,y):
            while y:
                x,y=y,x%y
            return abs(x)
        cur=head
        while cur and cur.next:
            n1=cur.val
            node2=cur.next
            n2=node2.val
            g=gcd(n1,n2)
            newnode=ListNode(g)
            newnode.next=node2
            cur.next=newnode
            cur=newnode.next
        return head

    