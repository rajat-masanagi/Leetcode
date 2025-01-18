# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self,n1,n2):
        m=min(n1,n2)
        for i in range(m,0,-1):
            if n1%i==0 and n2%i==0:
                return i
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur and cur.next:
            n1=cur.val
            node2=cur.next
            n2=node2.val
            gcd=self.gcd(n1,n2)
            newnode=ListNode(gcd)
            newnode.next=node2
            cur.next=newnode
            cur=newnode.next
        return head

    