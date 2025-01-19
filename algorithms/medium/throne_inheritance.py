# =======================================================================================
# The first algorithm is very slow for huge trees because we do DFS every time there
# is a birth or a death! We should be able to go directly to the node in case of a birth
# or death. I have simply created a top level object and that is slow. Each royal person
# node should be in a dictionary.
#
class Royalty:
    def __init__(self, name, is_alive=True, children=list()):
        self.name = name
        self.is_alive = is_alive
        self.children = children
        
class ThroneInheritance:
    def __init__(self, kingName: str):
        self.royalty = Royalty(kingName, True, list())

    def birth(self, parentName: str, childName: str) -> None:
        def dfs(node):
            if node.name == parentName:
                royalty = Royalty(childName, True, list())
                node.children.append(royalty)
                return
            for child in node.children:
                dfs(child)
        dfs(self.royalty)

    def death(self, name: str) -> None:
        def dfs(node):
            if node.name == name:
                node.is_alive = False
                return
            for child in node.children:
                dfs(child)
        dfs(self.royalty)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node):
            if node.is_alive:
                self.res.append(node.name)
            for child in node.children:
                dfs(child)
        self.res = list()
        dfs(self.royalty)
        return self.res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

# =======================================================================================
# The second algorithm below is much cleaner and faster. The defaultdict results in O(1)
# access to any node in case of birth/death. Also, no additional attributes are needed, so
# we can work with plain strings instead of objects.
#

from collections import defaultdict
class ThroneInheritance:
    def __init__(self, kingName: str):
        self.royalty = defaultdict(list)
        self.royalty[kingName] = list()
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.royalty[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node):
            if node not in self.dead:
                res.append(node)
            for child in self.royalty[node]:
                dfs(child)
        res = list()
        dfs(self.king)
        return res

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()



