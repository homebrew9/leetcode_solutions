class MyHashMap:

    def __init__(self):
        self.prime = 130729
        self.hm = [[] for _ in range(self.prime)]
    
    def get_hash(self, k):
        return k % self.prime

    def put(self, key: int, value: int) -> None:
        h = self.get_hash(key)
        if len(self.hm[h]) == 0:
            self.hm[h].append((key, value))
        else:
            for i, v in enumerate(self.hm[h]):
                if v[0] == key:
                    self.hm[h][i] = (key, value)

    def get(self, key: int) -> int:
        h = self.get_hash(key)
        if len(self.hm[h]) == 0:
            return -1
        else:
            for i, v in enumerate(self.hm[h]):
                if v[0] == key:
                    return v[1]
            return -1

    def remove(self, key: int) -> None:
        h = self.get_hash(key)
        ind = -1
        key_found = False
        for i, v in enumerate(self.hm[h]):
            if v[0] == key:
                key_found = True
                ind = i
                break
        if key_found:
            del self.hm[h][ind]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

