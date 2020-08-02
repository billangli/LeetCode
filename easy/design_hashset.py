class Node:
    
    def __init__(self, item: int):
        self.item = item
        self.next = None
        
    def append(self, item: int):
        curr = self
        while curr.next is not None:
            if curr.item == item:
                return
            curr = curr.next
        if curr.item != item:
            curr.next = Node(item)
        
    def remove(self, item: int) -> 'Node':
        """
        Remove Node containing item if it exists and return the head
        """
        curr = self
        if curr.item == item:
            return curr.next
        while curr.next is not None and curr.next.item != item:
            curr = curr.next
        if curr.next is not None:
            curr.next = curr.next.next
        return self
    
    def contains(self, item: int) -> bool:
        curr = self
        while curr is not None:
            if curr.item == item:
                return True
            curr = curr.next
        return False
        

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * 1024
        
    def _hash(self, key: int) -> int:
        """
        Return the hash of the key
        """
        return key & 0x3ff

    def add(self, key: int) -> None:
        hash_index = self._hash(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = Node(key)
        else:
            self.table[hash_index].append(key)
        
    def remove(self, key: int) -> None:
        hash_index = self._hash(key)
        if self.table[hash_index] is not None:
            self.table[hash_index] = self.table[hash_index].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_index = self._hash(key)
        return self.table[hash_index].contains(key) if self.table[hash_index] else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)