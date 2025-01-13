class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def createCLL(arr):
    head = ListNode(arr[0])
    node = head
    for i in range(1, len(arr)):
        node.next = ListNode(arr[i])
        node = node.next
    node.next = head
    return head

def printCLL(head):
    st = set()
    while head not in st:
        print(head.val)
        st.add(head)
        head = head.next

def josephus_cll(n):
    # Solving the Josephus problem using circular linked list
    arr = [i for i in range(1, n+1)]
    head = createCLL(arr)
    node = head
    while node.next != node:
        # Kill the next node and move on to next to next node
        node.next = node.next.next
        node = node.next
    return node.val

def josephus_pot(n):
    # Solving the Josephus problem using power of two
    x = -1 
    while pow(2, x+1) <= n:
        x += 1
    n -= 2**x
    return 2*n + 1

def josephus_bin(n):
    # Solving the Josephus problem using bit shifting
    b = bin(n)[2:]
    b = b[1:] + '1'
    return int(b, 2)

def josephus_lst(n):
    if n == 1:
        return 1
    arr = ['A' for _ in range(n)]
    i = 0
    strike = 0
    killed = 0
    runs = 0
    gameover = False
    while True:
        if gameover:
            break
        #print(f'\ti, arr[i] = {i}, {arr[i]}')
        while strike < n:
            strike = (strike + 1)%n
            if arr[strike] == 'A':
                arr[strike] = 'D'
                killed += 1
                #print(f'\t\tKilled => {strike}; Total killed = {killed}')
                if killed == n - 1:
                    gameover = True
                    break
                found = False
                while strike < n:
                    strike = (strike + 1)%n
                    if arr[strike] == 'A':
                        found = True
                        #print(f'\t\tHandover to => {strike}')
                        break
            if found:
                break
        i = (i + 1)%n
        #runs += 1
        #if runs % n == 0:
        #    print(f'===================')
    #print(f'arr = {arr}')
    for i in range(n):
        if arr[i] == 'A':
            return i + 1

# Main section
for n in range(1, 101):
    j1 = josephus_cll(n)
    j2 = josephus_pot(n)
    j3 = josephus_bin(n)
    j4 = josephus_lst(n)
    print('%4d : %4d %4d %4d %4d'%(n, j1, j2, j3, j4))
    #print('%4d : %4d %4d %4d'%(n, j1, j2, j3))


