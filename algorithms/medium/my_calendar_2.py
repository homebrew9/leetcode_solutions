from sortedcontainers import SortedList
class MyCalendarTwo:
    '''
      [10,20],[15,30],[25,35]
    '''
    def __init__(self):
        self.sl = SortedList()

    def book(self, start: int, end: int) -> bool:
        #print(f'start, end = {start}, {end}')
        if len(self.sl) <= 1:
            self.sl.add([start, end])
            return True
        e_min = None
        for s, e in self.sl:
            #print(f'\ts, e, e_min = {s}, {e}, {e_min}')
            if s >= end:
                e_min = None
                break
            if (s <= start < e) or (s < end <= e) or (start <= s < end) or (start < e <= end):
                if e_min and s < e_min:
                    return False
                e_min = min(end, e)
        self.sl.add([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

for arr_ops, arr_param, arr_exp in [
             (['MyCalendarTwo','book','book','book','book','book','book'], [[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]], [None,True,True,True,False,True,True]),
             (['MyCalendarTwo','book','book','book','book','book','book','book'], [[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55],[20,26]], [None,True,True,True,False,True,True,False]),
             (['MyCalendarTwo','book','book','book','book','book','book','book','book','book','book'], [[],[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]], [None,True,True,False,True,True,True,True,True,True,True]),
             (['MyCalendarTwo','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book','book'], [[],[5,12],[42,50],[4,9],[33,41],[2,7],[16,25],[7,16],[6,11],[13,18],[38,43],[49,50],[6,15],[5,13],[35,42],[19,24],[46,50],[39,44],[28,36],[28,37],[20,29],[41,49],[11,19],[41,46],[28,37],[17,23],[22,31],[4,10],[31,40],[4,12],[19,26]], [None,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False]),
        ]:
    print(f'arr_ops, arr_param, arr_exp = {arr_ops}, {arr_param}, {arr_exp}')
    for ops, param, exp in zip(arr_ops, arr_param, arr_exp):
        if ops == 'MyCalendarTwo':
            print(f'{ops}')
            obj = MyCalendarTwo()
        elif ops == 'book':
            print(f'{ops}{param}')
            r = obj.book(param[0], param[1])
            print(f'r, exp = {r}, {exp}')
            assert(r == exp)
        print('~~~~~~~')
    print('=====================')



