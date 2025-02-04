#
# This implementation of LRU Cache has been done by using a Double Linked List (DLL) to store the values
# and a dictionary to hold the keys. Each value in the dictionary is actually a pointer to the corresponding
# node in the DLL. Furthermore, we keep track of head and tail of the DLL. Thus, accessing the node is O(1),
# moving it to the end is also O(1). Every time we execute a "get", we move the node to the end - it is the
# most recent one. The least recent node is at the beginning (to the left) and it is evicted when the dictionary
# length exceeds the capacity of the LRU cache.
#
class ListNode:
    # Template for a double linked list
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None
        self.tail = None
        self.hsh = dict()

    def get(self, key: int) -> int:
        if key not in self.hsh:
            return -1
        curr_node = self.hsh[key]
        res = curr_node.val[1]
        next_node = curr_node.next
        if not next_node:
            return res
        if key == self.head:
            self.head = next_node.val[0]
        next_node.prev = curr_node.prev
        prev_node = curr_node.prev
        if prev_node:
            prev_node.next = curr_node.next
        tail_node = self.hsh[self.tail]
        tail_node.next = curr_node
        curr_node.prev = tail_node
        curr_node.next = None
        self.tail = key
        #self.display()
        return res

    def put(self, key: int, value: int) -> None:
        if key in self.hsh:
            self.hsh[key].val[1] = value
            self.get(key)
            return
        new_node = ListNode(val = [key, value])
        #print(f'\tnew_node, new_node.val = {new_node}, {new_node.val}')
        if self.head is None and self.tail is None:
            self.head = self.tail = key
            self.hsh[key] = new_node
            #self.display()
            return
        tail_node = self.hsh[self.tail]
        tail_node.next = new_node
        new_node.prev = tail_node
        self.tail = key
        self.hsh[key] = new_node
        if len(self.hsh) > self.cap:
            head_node = self.hsh[self.head]
            new_head = head_node.next.val[0]
            head_node.next.prev = None
            head_node.next = None
            del self.hsh[self.head]
            self.head = new_head
        #self.display()
    
    def display(self):
        print('hsh = ', [k for k in self.hsh.keys()])
        print('hsh1 = ', [v.val for v in self.hsh.values()])
        print('dll = ')
        test_head_node = self.hsh[self.head]
        while test_head_node:
            print(test_head_node.val, test_head_node.prev, test_head_node.next)
            test_head_node = test_head_node.next
        print('~~~')
        test_tail_node = self.hsh[self.tail]
        while test_tail_node:
            print(test_tail_node.val, test_tail_node.prev, test_tail_node.next)
            test_tail_node = test_tail_node.prev
        print('@@@')
        print(f'head, tail = {self.head}, {self.tail}')
        print('==========')
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Main section
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
["LRUCache","put","get"]
[[1],[2,1],[2]]
["LRUCache","put","put","get","put","put","get"]
[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]
["LRUCache","put","put","get","put","get","get"]
[[2],[2,1],[1,1],[2],[4,1],[1],[2]]

