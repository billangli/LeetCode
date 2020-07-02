# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iterative
        #
        # prev = None
        # curr = head
        # while curr is not None:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return curr
        
        # Recursive
        if head is None:
            return head
        
        temp = head.next
        head.next = None
        result = self.reverseList(temp)
        if result is None:
            return head
        
        temp.next = head
        return result
