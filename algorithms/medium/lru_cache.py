from sortedcontainers import SortedList
class LRUCache:

    def __init__(self, capacity: int):
        self.sl = SortedList()
        self.capacity = capacity
        self.hsh = dict()
        self.hsh_size = 0

    def get(self, key: int) -> int:
        #print(f'\tinside get: key, sl, hsh = {key}, {self.sl}, {self.hsh}')
        if key not in self.hsh:
            return -1
        val, freq = self.hsh[key]
        self.sl.remove((freq, key))
        max_freq = 0 if not self.sl else self.sl[-1][0]
        self.sl.add((max_freq+1, key))
        self.hsh[key] = (val, max_freq+1)
        return val

    def put(self, key: int, value: int) -> None:
        #print(f'\tinside put: key, value, sl, hsh = {key}, {value}, {self.sl}, {self.hsh}')
        if key in self.hsh:
            _, freq = self.hsh[key]
            max_freq, _ = self.sl[-1]
            self.sl.remove((freq, key))
            self.sl.add((max_freq+1, key))
            self.hsh[key] = (value, max_freq+1)
        else:
            if self.hsh_size < self.capacity:
                max_freq = 0 if not self.sl else self.sl[-1][0]
                self.sl.add((max_freq+1, key))
                self.hsh[key] = (value, max_freq+1)
                self.hsh_size += 1
            else:
                _, k = self.sl[0]
                del self.hsh[k]
                self.sl.pop(0)
                max_freq = 0 if not self.sl else self.sl[-1][0]
                self.sl.add((max_freq+1, key))
                self.hsh[key] = (value, max_freq+1)


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

