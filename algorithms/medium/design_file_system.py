from collections import defaultdict

class FileSystem:
    def __init__(self):
        self.hsh = defaultdict(int)

    def createPath(self, path: str, value: int) -> bool:
        if path in self.hsh:
            return False
        arr = path.split('/')
        if len(arr) > 2 and '/'.join(arr[:-1]) not in self.hsh:
            return False
        self.hsh[path] = value
        return True

    def get(self, path: str) -> int:
        return self.hsh.get(path, -1)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# Main section
#  ["FileSystem","createPath","get"]
#  [[],["/a",1],["/a"]]
#  ["FileSystem","createPath","createPath","get","createPath","get"]
#  [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]








