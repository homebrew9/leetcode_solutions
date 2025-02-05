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
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Checking out the diagram of the multilevel DLL and trying it out on paper
        # should make the recursion easy to understand. If we see a child node, then
        # we simply pass it to the recursive procedure. The procedure returns (head, tail).
        # We then fit the newly returned list in our current list.
        # Also, setting the child to None is very important.
        def solve(head):
            tail = None
            node = head
            while node:
                tail = node if not tail else tail.next
                if node.child is not None:
                    first, last = solve(node.child)
                    if node.next:
                        last.next = node.next
                        node.next.prev = last
                    node.next = first
                    first.prev = node
                    node.child = None  # This is *very* important!!
                node = node.next
            return (head, tail)
        if not head:
            return None
        first, last = solve(head)
        return first

# Test cases
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
[1,2,null,3]
[]
