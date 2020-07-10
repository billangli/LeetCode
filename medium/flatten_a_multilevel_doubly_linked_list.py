"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        prehead = Node(0, None, None, None)
        curr = prehead
        stack = [head]
        while len(stack):
            node = stack.pop()
            if node is not None:
                stack.append(node.next)
                stack.append(node.child)
                node.next = None
                node.child = None
                curr.next = node
                node.prev = curr
                curr = node
        if prehead.next is not None:
            prehead.next.prev = None
        return prehead.next
