class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = [None for _ in range(k)]
        self.head, self.tail = None, None
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.head is None and self.tail is None:
            self.arr[0] = value
            self.head, self.tail = 0, 0
            return True
        if (self.tail+1)%self.size == self.head:
            return False
        nextPos = (self.tail+1)%self.size
        self.arr[nextPos] = value
        self.tail = nextPos
        return True

    def deQueue(self) -> bool:
        if self.head is None and self.tail is None:
            return False
        if self.head == self.tail:
            self.arr[self.head] = None
            self.head, self.tail = None, None
            return True
        nextPos = (self.head+1)%self.size
        self.arr[self.head] = None
        self.head = nextPos
        return True

    def Front(self) -> int:
        if self.head is None and self.tail is None:
            return -1
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.head is None and self.tail is None:
            return -1
        return self.arr[self.tail]

    def isEmpty(self) -> bool:
        if self.head is None and self.tail is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.head is None and self.tail is None:
            return False
        if (self.tail+1)%self.size == self.head:
            return True
        return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# ==============================================
# Main section
#  mcq = MyCircularQueue(3)
#  r = mcq.enQueue(1); # return True
#  print(f'r = {r}')
#  r = mcq.enQueue(2); # return True
#  print(f'r = {r}')
#  r = mcq.enQueue(3); # return True
#  print(f'r = {r}')
#  r = mcq.enQueue(4); # return False
#  print(f'r = {r}')
#  r = mcq.Rear();     # return 3
#  print(f'r = {r}')
#  r = mcq.isFull();   # return True
#  print(f'r = {r}')
#  r = mcq.deQueue();  # return True
#  print(f'r = {r}')
#  r = mcq.enQueue(4); # return True
#  print(f'r = {r}')
#  r = mcq.Rear();     # return 4
#  print(f'r = {r}')
#  print('===================================')

#["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","deQueue","deQueue","isEmpty","isEmpty","Rear","Rear","deQueue"]
#[[8],              [3],      [9],      [5],      [0],      [],       [],        [],       [],      [],    [],    []]

#    mcq = MyCircularQueue(8)
#    r = mcq.enQueue(3)
#    print(f'r = {r}')
#    r = mcq.enQueue(9)
#    print(f'r = {r}')
#    r = mcq.enQueue(5)
#    print(f'r = {r}')
#    r = mcq.enQueue(0)
#    print(f'r = {r}')
#    r = mcq.deQueue()
#    print(f'r = {r}')
#    r = mcq.deQueue()
#    print(f'r = {r}')
#    r = mcq.isEmpty()
#    print(f'r = {r}')
#    r = mcq.isEmpty()
#    print(f'r = {r}')
#    r = mcq.Rear()
#    print(f'r = {r}')
#    r = mcq.Rear()
#    print(f'r = {r}')
#    r = mcq.deQueue()
#    print(f'r = {r}')
#    print('===================================')

for ops, data in [
                    (['MyCircularQueue','enQueue','deQueue','isFull','enQueue','Front','Front','enQueue','deQueue','enQueue','Rear','isFull','Front','enQueue','enQueue','deQueue','Rear','Front','Front','deQueue','enQueue','enQueue','Front','deQueue','deQueue','enQueue','deQueue','enQueue','Front','deQueue','enQueue','deQueue','Rear','Front','Front','deQueue','Front','isFull','Front','enQueue','enQueue','deQueue','enQueue','Front','enQueue','enQueue','enQueue','Rear','enQueue','deQueue','enQueue','deQueue','enQueue','deQueue','isEmpty','enQueue','enQueue','enQueue','Rear','enQueue','enQueue','Rear','isEmpty','Rear','Front','Front','enQueue','isEmpty','Rear','deQueue','Rear','deQueue','enQueue','enQueue','deQueue','enQueue','enQueue','Front','Rear','enQueue','deQueue','deQueue','Front','enQueue','enQueue','Front','enQueue','isFull','enQueue','Rear','Front','Front','enQueue','deQueue','deQueue','enQueue','Rear','Front','Rear','enQueue','enQueue','Rear','Front','Rear','deQueue','deQueue','enQueue','Rear','enQueue','enQueue','enQueue','deQueue','enQueue','isEmpty','Rear','Front','enQueue','isEmpty','Rear','enQueue','deQueue','Rear','Front','deQueue','deQueue','enQueue','deQueue','Rear','Rear','Front','enQueue','Rear','Rear','enQueue','Rear','Rear','enQueue','enQueue','Rear','isEmpty','enQueue','deQueue','deQueue','Rear','enQueue','isEmpty','Rear','Rear','enQueue','enQueue','Rear','Front','isEmpty','Rear','deQueue','enQueue','Front','Rear','enQueue','enQueue','Front','deQueue','enQueue','Rear','enQueue','enQueue','enQueue','enQueue','isFull','Rear','enQueue','deQueue','enQueue','enQueue','Rear','Rear','isFull','enQueue','deQueue','enQueue','enQueue','deQueue','Rear','isEmpty','enQueue','enQueue','enQueue','Rear','Rear','Front','Front','Rear','enQueue','deQueue','Rear','enQueue','isFull','enQueue','Rear','enQueue','Rear','Rear','Front','enQueue','enQueue','Rear','Front','isEmpty','deQueue','deQueue','Front','isFull','deQueue','Rear','Rear','Rear','deQueue','enQueue','enQueue','Rear','enQueue','Front','enQueue','enQueue','enQueue','deQueue','Rear','enQueue','Front','enQueue','Front','enQueue','Front','deQueue','Front','enQueue','enQueue','Front','Front','Rear','Rear','isEmpty','Rear','Rear','enQueue','Front','Front','Rear','Rear','enQueue','enQueue','Front','Front','enQueue','Front','enQueue','enQueue','Rear','isEmpty','Rear','Rear','enQueue','Rear','enQueue','Front','deQueue','Rear','enQueue','Front','enQueue','Rear','Rear','Front','enQueue','deQueue','Front','enQueue','enQueue','enQueue','Front','deQueue','enQueue','enQueue','Front','enQueue','Front','Front','deQueue','enQueue','Front','enQueue','enQueue','Front','Rear','isEmpty','deQueue','Rear','enQueue','enQueue','Front','Front','Front','Front','enQueue','isFull','isFull','enQueue','Front','isFull','Rear','enQueue','enQueue','enQueue','deQueue','deQueue','isFull','Front','Rear','deQueue','enQueue','Rear','enQueue','enQueue','deQueue','isFull','isFull','enQueue','enQueue','Front','Front','Front','Front','enQueue','Front','Front','enQueue','Front','Rear','Rear','enQueue','deQueue','isEmpty','enQueue','deQueue','Front','Rear','Front','Front','deQueue','enQueue','Rear','enQueue','deQueue','deQueue','deQueue','enQueue','enQueue','Front','deQueue','Front','enQueue','enQueue','Rear','deQueue','Rear','enQueue','enQueue','enQueue','enQueue','isFull','Rear','Rear','enQueue','isEmpty','Front','Rear','enQueue','deQueue','Rear','Front','deQueue','enQueue','Rear','Rear','enQueue','deQueue','enQueue','deQueue','Front','isEmpty','deQueue','enQueue','Front','enQueue','enQueue','deQueue','isEmpty','Front','Front','enQueue','Rear','Front','enQueue','Front','Front','enQueue','deQueue','enQueue','enQueue','deQueue','isFull','isEmpty','enQueue','Front','Rear','Rear','enQueue','Rear','deQueue','Rear','isFull','deQueue','enQueue','deQueue','isFull','Rear','isEmpty','enQueue','Rear','Rear','Rear','enQueue','Front','deQueue','enQueue','Front','enQueue','isFull','Front','Rear','deQueue','Front','enQueue','enQueue','deQueue','Rear','Rear','enQueue','Front','isEmpty','Rear','enQueue','deQueue','Front','enQueue','Front','Front','Rear','enQueue','enQueue','Front','enQueue','Front','deQueue','deQueue','isFull','Front','Front','Front','Rear','enQueue','deQueue','Rear','Rear','enQueue','Front','Front','deQueue','Front','Rear','deQueue','Rear','Front','enQueue','Rear','enQueue','Front','Rear','deQueue','enQueue','enQueue','Front','Rear','enQueue','enQueue','Front','enQueue','deQueue','Front','Rear','enQueue','Rear','isFull','Rear','enQueue','isFull','isEmpty','Rear','enQueue','enQueue','Front','Front','Rear','Front','enQueue','Front','Front','enQueue','Rear','enQueue','Front','Front','Rear','isFull','isFull','enQueue','Rear','isEmpty','Front','Rear','enQueue','enQueue','enQueue','Front','Front','enQueue','Front','enQueue','enQueue','Front','Front','deQueue','enQueue','deQueue','Rear','Front','enQueue','Front','isEmpty','Front','Rear','enQueue','deQueue','enQueue','Rear','enQueue','Front','enQueue','deQueue','enQueue','isFull','enQueue','Front','Rear','isFull','Rear','Rear','Rear','enQueue','Rear','Rear','Rear','enQueue','enQueue','enQueue','Rear','enQueue','isFull','Front','enQueue','Rear','isFull','Front','Rear','Front','enQueue','deQueue','Rear','enQueue','Rear','Front','isFull','Front','Front','isFull','Rear','deQueue','enQueue','enQueue','deQueue','deQueue','isEmpty','enQueue','isEmpty','enQueue','enQueue','enQueue','enQueue','Rear','enQueue','Rear','deQueue','Front','enQueue','Rear','Front','enQueue','Rear','Front','enQueue','Rear','Front','Rear','Front','Rear','Front','Front','deQueue','enQueue','deQueue','Rear','isFull','enQueue','Rear','Front','Rear','enQueue','enQueue','enQueue','deQueue','Rear','enQueue','enQueue','deQueue','isEmpty','Rear','enQueue','isFull','Rear','isEmpty','isFull','deQueue','Rear','Front','deQueue','deQueue','enQueue','Rear','Front','Rear','enQueue','isFull','Rear','deQueue','deQueue','enQueue','enQueue','isFull','Front','enQueue','Rear','deQueue','Rear','Front','Front','enQueue','enQueue','enQueue','enQueue','enQueue','enQueue','deQueue','enQueue','enQueue','Rear','Front','Rear','Front','enQueue','Rear','Front','isFull','Rear','Rear','Front','Front','Rear','deQueue','enQueue','Front','enQueue','deQueue','Front','enQueue','enQueue','enQueue','enQueue','Rear','enQueue','Front','enQueue','Rear','Rear','enQueue','Front','enQueue','Front','Front','Rear','enQueue','Rear','enQueue','Front','isFull','isFull','Rear','deQueue','deQueue','Front','deQueue','enQueue','Rear','Rear','enQueue','isFull','enQueue','isFull','enQueue','enQueue','enQueue','Front','enQueue','enQueue','Front','Front','Rear','Rear','deQueue','Rear','enQueue','isEmpty','enQueue','Front','enQueue','enQueue','enQueue','Front','Front','Rear','enQueue','isEmpty','enQueue','deQueue','Front','deQueue','Front','enQueue','enQueue','enQueue','Rear','deQueue','Front','Rear','deQueue','enQueue','isEmpty','Rear','enQueue','enQueue','Rear','enQueue','Front','deQueue','enQueue','deQueue','Front','deQueue','Front','enQueue','enQueue','Front','enQueue','enQueue','Front','Rear','enQueue','isEmpty','Rear','enQueue','deQueue','deQueue','Rear','enQueue','Front','Front','enQueue','deQueue','Front','enQueue','deQueue','Rear','Rear','Front','deQueue','isEmpty','enQueue','deQueue','deQueue','Rear','enQueue','deQueue','Rear','isFull','enQueue','enQueue','Front','deQueue','Front','enQueue','deQueue','enQueue','enQueue','enQueue','Rear','isFull','Front','enQueue','Rear','enQueue','Rear','Rear','Front','Rear','deQueue','enQueue','isFull','Rear','Front','Rear','Front','isFull','enQueue','Front','enQueue','Front','Rear','Rear','Rear','enQueue','deQueue','deQueue','Front','enQueue','enQueue','Front','Rear','Rear','enQueue','Front','enQueue','enQueue','isEmpty','Front','enQueue','enQueue','Front','enQueue','isEmpty','enQueue','enQueue','deQueue','enQueue','deQueue','Front','Front','Rear','Rear','deQueue','deQueue','Front','deQueue','isFull','deQueue','enQueue','enQueue','isFull','enQueue','Rear','Rear','Rear','Front','Front','enQueue','enQueue','Front','Rear','enQueue','Rear','deQueue','deQueue','enQueue','Front','Front','Front','isEmpty','Front','enQueue','Rear','isFull','Rear','enQueue','enQueue','isEmpty','isEmpty','isFull','enQueue','deQueue','Front','enQueue','Rear','Rear','Rear','deQueue','Front','deQueue','Front','deQueue','Front','Front','enQueue','deQueue','deQueue','enQueue','enQueue','Front','enQueue','Front','Front','enQueue','Front','enQueue','deQueue','enQueue','enQueue','isFull','deQueue','Rear','enQueue','Rear','Rear','Front','Front','enQueue','Front','Front','Front','Front','enQueue','enQueue','Rear','enQueue','Front','Rear','isFull','Rear','Rear','deQueue','deQueue','enQueue','enQueue','enQueue','Rear','enQueue','Rear','Rear','Rear','deQueue','Front','Rear','deQueue','deQueue','Rear','Front','enQueue','isFull','deQueue','Rear','deQueue','Front','Front','Front','Rear'], [[496],[255],[],[],[37],[],[],[505],[],[524],[],[],[],[395],[480],[],[],[],[],[],[451],[799],[],[],[],[533],[],[695],[],[],[575],[],[],[],[],[],[],[],[],[460],[472],[],[914],[],[310],[594],[126],[],[130],[],[454],[],[803],[],[],[291],[734],[187],[],[682],[407],[],[],[],[],[],[415],[],[],[],[],[],[696],[555],[],[830],[211],[],[],[379],[],[],[],[322],[712],[],[886],[],[573],[],[],[],[573],[],[],[312],[],[],[],[615],[516],[],[],[],[],[],[878],[],[728],[971],[967],[],[566],[],[],[],[193],[],[],[708],[],[],[],[],[],[942],[],[],[],[],[406],[],[],[662],[],[],[934],[884],[],[],[760],[],[],[],[813],[],[],[],[824],[271],[],[],[],[],[],[616],[],[],[651],[499],[],[],[807],[],[823],[680],[621],[652],[],[],[138],[],[877],[221],[],[],[],[665],[],[296],[587],[],[],[],[270],[631],[775],[],[],[],[],[],[627],[],[],[547],[],[433],[],[737],[],[],[],[867],[161],[],[],[],[],[],[],[],[],[],[],[],[],[958],[191],[],[58],[],[292],[157],[854],[],[],[886],[],[471],[],[63],[],[],[],[483],[734],[],[],[],[],[],[],[],[432],[],[],[],[],[497],[354],[],[],[436],[],[400],[360],[],[],[],[],[7],[],[986],[],[],[],[572],[],[827],[],[],[],[835],[],[],[31],[244],[549],[],[],[910],[182],[],[92],[],[],[],[194],[],[912],[492],[],[],[],[],[],[379],[892],[],[],[],[],[328],[],[],[303],[],[],[],[614],[632],[669],[],[],[],[],[],[],[35],[],[97],[365],[],[],[],[711],[373],[],[],[],[],[324],[],[],[277],[],[],[],[259],[],[],[728],[],[],[],[],[],[],[923],[],[804],[],[],[],[20],[399],[],[],[],[945],[803],[],[],[],[850],[372],[676],[774],[],[],[],[556],[],[],[],[220],[],[],[],[],[118],[],[],[365],[],[507],[],[],[],[],[490],[],[512],[330],[],[],[],[],[235],[],[],[878],[],[],[5],[],[787],[6],[],[],[],[753],[],[],[],[103],[],[],[],[],[],[415],[],[],[],[],[341],[],[],[],[442],[],[],[614],[],[571],[],[],[],[],[],[565],[678],[],[],[],[912],[],[],[],[179],[],[],[431],[],[],[],[221],[367],[],[497],[],[],[],[],[],[],[],[],[373],[],[],[],[364],[],[],[],[],[],[],[],[],[453],[],[445],[],[],[],[937],[81],[],[],[23],[224],[],[815],[],[],[],[856],[],[],[],[964],[],[],[],[85],[650],[],[],[],[],[804],[],[],[699],[],[440],[],[],[],[],[],[283],[],[],[],[],[557],[642],[689],[],[],[230],[],[689],[957],[],[],[],[728],[],[],[],[195],[],[],[],[],[165],[],[128],[],[189],[],[689],[],[836],[],[700],[],[],[],[],[],[],[500],[],[],[],[414],[36],[12],[],[564],[],[],[790],[],[],[],[],[],[507],[],[],[804],[],[],[],[],[],[],[],[],[974],[195],[],[],[],[794],[],[165],[356],[283],[145],[],[303],[],[],[],[155],[],[],[327],[],[],[289],[],[],[],[],[],[],[],[],[591],[],[],[],[664],[],[],[],[893],[345],[111],[],[],[417],[70],[],[],[],[226],[],[],[],[],[],[],[],[],[],[814],[],[],[],[672],[],[],[],[],[390],[553],[],[],[215],[],[],[],[],[],[680],[168],[800],[678],[188],[384],[],[362],[505],[],[],[],[],[335],[],[],[],[],[],[],[],[],[],[430],[],[582],[],[],[329],[972],[786],[771],[],[215],[],[870],[],[],[17],[],[656],[],[],[],[750],[],[973],[],[],[],[],[],[],[],[],[84],[],[],[482],[],[72],[],[560],[529],[845],[],[600],[973],[],[],[],[],[],[],[448],[],[646],[],[218],[307],[840],[],[],[],[587],[],[205],[],[],[],[],[199],[881],[893],[],[],[],[],[],[956],[],[],[133],[796],[],[704],[],[],[61],[],[],[],[],[811],[83],[],[702],[375],[],[],[662],[],[],[362],[],[],[],[650],[],[],[444],[],[],[312],[],[],[],[],[],[],[701],[],[],[],[413],[],[],[],[234],[328],[],[],[],[692],[],[766],[161],[825],[],[],[],[412],[],[716],[],[],[],[],[],[497],[],[],[],[],[],[],[733],[],[581],[],[],[],[],[940],[],[],[],[745],[772],[],[],[],[243],[],[205],[77],[],[],[891],[79],[],[689],[],[461],[134],[],[745],[],[],[],[],[],[],[],[],[],[],[],[489],[287],[],[952],[],[],[],[],[],[476],[189],[],[],[55],[],[],[],[154],[],[],[],[],[],[154],[],[],[],[486],[588],[],[],[],[84],[],[],[623],[],[],[],[],[],[],[],[],[],[],[49],[],[],[805],[15],[],[442],[],[],[970],[],[799],[],[201],[782],[],[],[],[143],[],[],[],[],[242],[],[],[],[],[903],[285],[],[232],[],[],[],[],[],[],[],[768],[894],[356],[],[788],[],[],[],[],[],[],[],[],[],[],[924],[],[],[],[],[],[],[],[]]),
                 ]:
    #print(f'ops, data = {ops}, {data}')
    for o, d in zip(ops, data):
        if o == 'MyCircularQueue':
            mcq = MyCircularQueue(d[0])
        elif o == 'enQueue':
            r = mcq.enQueue(d[0])
            print(f'r = {r}')
        elif o == 'deQueue':
            r = mcq.deQueue()
            print(f'r = {r}')
        elif o == 'Front':
            r = mcq.Front()
            print(f'r = {r}')
        elif o == 'Rear':
            r = mcq.Rear()
            print(f'r = {r}')
        elif o == 'isEmpty':
            r = mcq.isEmpty()
            print(f'r = {r}')
        elif o == 'isFull':
            r = mcq.isFull()
            print(f'r = {r}')
    print('===================================')



