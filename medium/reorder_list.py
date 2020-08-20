# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> 'ListNode':
        prev = None
        curr = head
        while curr is not None:
            curr.next, curr, prev = prev, curr.next, curr
        return prev
        
    def lenList(self, head: ListNode) -> int:
        count = 0
        curr = head
        while curr is not None:
            curr = curr.next
            count += 1
        return count
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """        
        if head is None: return None
        
        half_len = (self.lenList(head) + 1) // 2
        curr = head
        count = 0
        while count < half_len - 1:
            curr = curr.next
            count += 1
        
        first_head = head
        second_head = curr.next
        curr.next = None
        
        second_head = self.reverseList(second_head)
        while second_head is not None:
            first_head.next, second_head.next, second_head = second_head, first_head.next, second_head.next
            first_head = first_head.next.next
