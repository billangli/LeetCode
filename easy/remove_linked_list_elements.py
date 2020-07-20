# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val == val:
            head = head.next
            
        curr = head
        while curr is not None:
            next_ = curr.next
            while next_ is not None and next_.val == val:
                next_ = next_.next
            curr.next = next_
            curr = curr.next
            
        return head
