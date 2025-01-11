class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def printList(self, msg):
        cnt = 0
        node = self.head
        res = f'{msg} : '
        while node:
            cnt += 1
            res += str(node.val) + ' -> '
            node = node.next
        res += f' (self.size, actual_size = {self.size}, {cnt})'
        print(res)

    def get(self, index: int) -> int:
        self.printList(f'Inside get({index})')
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            return self.head.val
        if index == self.size - 1:
            return self.tail.val
        ind = 0
        node = self.head
        while node:
            node = node.next
            ind += 1
            if ind == index:
                print(f'=> Return value from get({index}) = {node.val}')
                return node.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
            self.size = 1
        else:
            newHead = Node(val)
            newHead.next = self.head
            self.head = newHead
            self.size += 1
        self.printList(f'After addAtHead({val})')
        
    def addAtTail(self, val: int) -> None:
        self.printList(f'=====\nInside addAtTail({val}), tail.val = {self.tail.val}')
        if not self.tail:
            self.head = Node(val)
            self.tail = self.head
            self.size = 1
        else:
            newTail = Node(val)
            self.tail.next = newTail
            self.tail = newTail
            self.size += 1
        self.printList(f'After addAtTail({val}), tail.val = {self.tail.val}')

    def addAtIndex(self, index: int, val: int) -> None:
        p_index = index
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        node = self.head
        prev = None
        while index > 0:
            prev = node
            node = node.next
            index -= 1
        newNode = Node(val)
        newNode.next = node
        prev.next = newNode
        self.size += 1
        self.printList(f'After addAtIndex({p_index}, {val})')

    def deleteAtIndex(self, index: int) -> None:
        p_index = index
        #self.printList(f'Inside deleteAtIndex({p_index})')
        if index < 0 or index >= self.size:
            return
        if index == 0:
            newHead = self.head.next
            self.head = newHead
            self.size -= 1
            self.printList(f'After deleteAtIndex({p_index})')
            return
        prev = None
        node = self.head
        while index > 0:
            prev = node
            node = node.next
            index -= 1
        # Very important: if we are deleting the tail node, then reset tail node!
        if p_index == self.size - 1:
            self.tail = prev
        prev.next = node.next
        self.size -= 1
        self.printList(f'After deleteAtIndex({p_index})')

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Main section
for ops, data in [
                    (['MyLinkedList','addAtHead','addAtTail','addAtTail','get','get','addAtTail','addAtIndex','addAtHead','addAtHead','addAtTail','addAtTail','addAtTail','addAtTail','get','addAtHead','addAtHead','addAtIndex','addAtIndex','addAtHead','addAtTail','deleteAtIndex','addAtHead','addAtHead','addAtIndex','addAtTail','get','addAtIndex','addAtTail','addAtHead','addAtHead','addAtIndex','addAtTail','addAtHead','addAtHead','get','deleteAtIndex','addAtTail','addAtTail','addAtHead','addAtTail','get','deleteAtIndex','addAtTail','addAtHead','addAtTail','deleteAtIndex','addAtTail','deleteAtIndex','addAtIndex','deleteAtIndex','addAtTail','addAtHead','addAtIndex','addAtHead','addAtHead','get','addAtHead','get','addAtHead','deleteAtIndex','get','addAtHead','addAtTail','get','addAtHead','get','addAtTail','get','addAtTail','addAtHead','addAtIndex','addAtIndex','addAtHead','addAtHead','deleteAtIndex','get','addAtHead','addAtIndex','addAtTail','get','addAtIndex','get','addAtIndex','get','addAtIndex','addAtIndex','addAtHead','addAtHead','addAtTail','addAtIndex','get','addAtHead','addAtTail','addAtTail','addAtHead','get','addAtTail','addAtHead','addAtTail','get','addAtIndex'], [[],[84],[2],[39],[3],[1],[42],[1,80],[14],[1],[53],[98],[19],[12],[2],[16],[33],[4,17],[6,8],[37],[43],[11],[80],[31],[13,23],[17],[4],[10,0],[21],[73],[22],[24,37],[14],[97],[8],[6],[17],[50],[28],[76],[79],[18],[30],[5],[9],[83],[3],[40],[26],[20,90],[30],[40],[56],[15,23],[51],[21],[26],[83],[30],[12],[8],[4],[20],[45],[10],[56],[18],[33],[2],[70],[57],[31,24],[16,92],[40],[23],[26],[1],[92],[3,78],[42],[18],[39,9],[13],[33,17],[51],[18,95],[18,33],[80],[21],[7],[17,46],[33],[60],[26],[4],[9],[45],[38],[95],[78],[54],[42,86]]),
                 ]:
    for o, d in zip(ops, data):
        if o == 'MyLinkedList':
            mll = MyLinkedList()
        elif o == 'addAtHead':
            r = mll.addAtHead(d[0])
        elif o == 'addAtTail':
            r = mll.addAtTail(d[0])
        elif o == 'get':
            r = mll.get(d[0])
            print(f'r = {r}')
        elif o == 'addAtIndex':
            r = mll.addAtIndex(d[0], d[1])
        elif o == 'deleteAtIndex':
            r = mll.deleteAtIndex(d[0])

