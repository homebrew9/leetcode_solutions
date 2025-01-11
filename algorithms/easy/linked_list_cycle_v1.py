#
# Ref: https://www.tutorialspoint.com/linked-list-cycle-in-python#
#
class ListNode:
   def __init__(self, data, next = None):
      self.data = data
      self.next = next
def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head
def get_node(head, pos):
   if pos != -1:
      p = 0
      ptr = head
      while p < pos:
         ptr = ptr.next
         p += 1
      return ptr
class Solution(object):
   def hasCycle(self, head):
      hashS = set()
      while head:
         if head in hashS:
            return True
         hashS.add(head)
         head = head.next
      return False

head = make_list([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5])
last_node = get_node(head, -21)
pos = -1
last_node.next = get_node(head, pos)
ob1 = Solution()
print(ob1.hasCycle(head))

