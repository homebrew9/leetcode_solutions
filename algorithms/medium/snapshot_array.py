class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = [[[0, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        #print(f'\tInside set; self.arr  = {self.arr}')
        self.arr[index].append([self.snap_id, val])
        #print(f'\tLeaving set; self.arr = {self.arr}')

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        lst = self.arr[index]
        #print('=====')
        #print(f'self.arr = {self.arr}')
        #print(f'lst      = {lst}')
        N = len(lst)
        left, right = 0, N - 1
        while left <= right:
            mid = (left + right) // 2
            if lst[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1
        return lst[right][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


'''
["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
'''


