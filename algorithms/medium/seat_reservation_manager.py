#
# Using an array would be too slow!! It throws TLE for arrays.
# Use heap instead.
#
import heapq
class SeatManager:

    def __init__(self, n: int):
        self.hp = [i for i in range(n)]
        heapq.heapify(self.hp)

    def reserve(self) -> int:
        n = heapq.heappop(self.hp)
        return n + 1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.hp, seatNumber - 1)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)

obj = SeatManager(5)

arr1 = ['reserve','reserve','unreserve','reserve','reserve','reserve','reserve','unreserve']
arr2 = [[],[],[2],[],[],[],[],[5]]
res = list()
for op, arr in zip(arr1, arr2):
    if op == 'reserve':
        r = obj.reserve()
        #print(f'r = {r}')
        res.append(r)
    elif op == 'unreserve':
        r = obj.unreserve(*arr)
        #print(f'r = {r}')
        res.append(r)
print(res)
print('===========')


