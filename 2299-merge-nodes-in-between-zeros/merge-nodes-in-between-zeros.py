# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head.next
        while cur:
            if cur.next.val!=0:
                cur.val+=cur.next.val
                cur.next=cur.next.next
            else:
                cur.next=cur.next.next
                cur=cur.next
        return head.next

            
        