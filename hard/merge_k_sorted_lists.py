# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        # The heap will store tuples (value, list_num)
        heap = []
        head = ListNode()
        curr = head
        
        for i in range(len(lists)):
            if lists[i] is not None:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while heap:
            value, list_num = heappop(heap)
            curr.next = ListNode(value)
            curr = curr.next
            
            if lists[list_num] is not None:
                heappush(heap, (lists[list_num].val, list_num))
                lists[list_num] = lists[list_num].next
        
        return head.next
