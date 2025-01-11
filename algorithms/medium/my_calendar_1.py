from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.sl = SortedList()

    def book(self, start: int, end: int) -> bool:
        print(start, end, self.sl)
        if len(self.sl) == 0:
            self.sl.add([start, end])
            return True
        if end <= self.sl[0][0]:
            self.sl.add([start, end])
            return True
        if start == self.sl[-1][1]:
            start1, end1 = self.sl[-1]
            self.sl.pop()
            self.sl.add([start1, end])
            return True
        if start > self.sl[-1][1]:
            self.sl.add([start, end])
            return True
        for i in range(1, len(self.sl)):
            s1, e1 = self.sl[i-1]
            s2, e2 = self.sl[i]
            if start >= e2:
                continue
            # So we have three intervals [s1,e1) <=> [start,end) <=> [s2,e2)
            # We can check if (start,end) can "fit in".
            print(f'\t({s1},{e1}), ({start},{end}), ({s2},{e2})')
            if start < e1 or end > s2:
                return False
            # There are 4 possibilities now, as seen below with examples:
            # [5,7] [7,10] [10,20]  => [5,20]
            # [5,7] [7,9]  [10,20]  => [5,9] [10,20]
            # [5,7] [8,10] [10,20]  => [5,7] [8,20]
            # [5,7] [8,9]  [10,20]  => [5,7] [8,9] [10,20]
            if e1 == start and end == s2:
                print(f'\t\tin if # 1...')
                del self.sl[i-1]
                del self.sl[i-1]
                self.sl.add([s1,e2])
                return True
            if e1 == start:
                print(f'\t\tin if # 2...')
                del self.sl[i-1]
                self.sl.add([s1,end])
                return True
            if end == s2:
                print(f'\t\tin if # 3...')
                del self.sl[i]
                self.sl.add([start,e2])
                return True
            print(f'\t\tin final else...')
            self.sl.add([start, end])
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


for arr_ops, arr_param, arr_exp in [
            #(['MyCalendar','book','book','book'], [[],[10,20],[15,25],[20,30]], [None,True,False,True]),
            #(['MyCalendar','book','book','book','book','book','book','book','book','book','book'], [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]], [None,True,True,False,False,True,False,True,True,True,False]),
            (['MyCalendar','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book'], [[],[69,70],[3,4],[39,40],[35,36],[3,4],[55,56],[61,62],[97,98],[79,80],[76,77],[46,47],[78,79],[47,48],[38,39],[83,84],[90,91],[90,91],[49,50],[49,50],[77,78],[23,24],[89,90],[8,9],[3,4],[2,3],[48,49],[96,97],[4,5],[54,55],[30,31],[97,98],[65,66],[93,94],[49,50],[24,25],[17,18],[53,54],[45,46],[53,54],[32,33],[37,38],[5,6],[50,51],[48,49],[14,15],[91,92],[79,80],[73,74],[28,29],[31,32],[98,99],[37,38],[19,20],[49,50],[54,55],[37,38],[98,99],[12,13],[24,25],[46,47],[74,75],[87,88],[64,65],[61,62],[68,69],[28,29],[43,44],[89,90],[64,65],[72,73],[69,70],[88,89],[68,69],[28,29],[20,21],[64,65],[17,18],[40,41],[88,89],[22,23],[8,9],[33,34],[13,14],[19,20],[53,54],[99,100],[24,25],[82,83],[77,78],[90,91],[72,73],[33,34],[73,74],[0,1],[25,26],[69,70],[73,74],[12,13],[33,34],[47,48],[26,27],[77,78],[95,96],[28,29],[77,78],[28,29],[87,88],[16,17],[42,43],[51,52],[44,45],[63,64],[24,25],[18,19],[0,1],[45,46],[65,66],[21,22],[37,38],[77,78],[97,98],[24,25],[83,84],[20,21],[29,30],[66,67],[29,30],[37,38],[63,64],[15,16],[85,86],[61,62],[0,1],[23,24],[96,97],[91,92],[90,91],[80,81],[18,19],[69,70],[3,4],[59,60],[21,22],[75,76],[54,55],[65,66],[34,35],[19,20],[79,80],[6,7],[24,25],[29,30],[35,36],[9,10],[0,1],[73,74],[65,66],[78,79],[32,33],[58,59],[25,26],[3,4],[78,79],[92,93],[37,38],[91,92],[5,6],[79,80],[94,95],[78,79],[38,39],[16,17],[81,82],[34,35],[16,17],[33,34],[42,43],[34,35],[89,90],[88,89],[33,34],[68,69],[92,93],[73,74],[64,65],[91,92],[44,45],[13,14],[97,98],[64,65],[31,32],[91,92],[1,2],[57,58],[21,22],[38,39],[70,71],[84,85],[50,51],[58,59]], [None,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False]),
        ]:
    print(f'arr_ops, arr_param, arr_exp = {arr_ops}, {arr_param}, {arr_exp}')
    for ops, param, exp in zip(arr_ops, arr_param, arr_exp):
        if ops == 'MyCalendar':
            print(f'{ops}')
            obj = MyCalendar()
        elif ops == 'book':
            print(f'{ops}{param}')
            r = obj.book(param[0], param[1])
            print(f'r, exp = {r}, {exp}')
        print('~~~~~~~')
    print('=====================')



