class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MRUQueue:
    def __init__(self, n: int):
        self.head = ListNode(1)
        node = self.head
        for i in range(2, n+1):
            new_node = ListNode(i)
            node.next = new_node
            node = new_node
        self.size = n
        self.tail = node

    def fetch(self, k: int) -> int:
        if k == self.size:
            return self.tail.val
        prev, curr = None, self.head
        for _ in range(k-1):
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next
        self.tail.next = curr
        curr.next = None
        self.tail = curr
        return self.tail.val

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)

# Test cases
# ["MRUQueue","fetch","fetch","fetch","fetch"]
# [[8],[3],[5],[2],[8]]
# ["MRUQueue","fetch","fetch","fetch","fetch","fetch","fetch","fetch","fetch","fetch","fetch"]
# [[3],[2],[1],[2],[2],[2],[3],[2],[1],[1],[2]]

