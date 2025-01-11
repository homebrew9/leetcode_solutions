from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def dfs(node):
            #print(f'\tnode, self.hsh_child, self.seen = {node}, {self.hsh_child}, {self.seen}')
            if node in self.hsh_child:
                for nextNode in self.hsh_child[node]:
                    if nextNode in self.seen:
                        self.isValid = False
                        break
                    self.seen.add(nextNode)
                    dfs(nextNode)
        self.hsh_child = dict()
        self.hsh_parent = dict()
        for i, (left, right) in enumerate(zip(leftChild, rightChild)):
            # Fill in hsh_child
            if left != -1:
                self.hsh_child[i] = [left]
            if right != -1:
                if i in self.hsh_child:
                    self.hsh_child[i] += [right]
                else:
                    self.hsh_child[i] = [right]
            # Fill in hsh_parent - a node can have only one parent
            if left != -1:
                if left in self.hsh_parent:
                    #print('Found an existing parent!')
                    return False
                self.hsh_parent[left] = i
            if right != -1:
                if right in self.hsh_parent:
                    #print('Found an existing parent!')
                    return False
                self.hsh_parent[right] = i
        #print(self.hsh_child)
        #print(self.hsh_parent)
        # Standalone nodes do not make a binary tree
        if len(self.hsh_child) == 0 or len(self.hsh_parent) == 0:
            if n == 1:
                return True
            else:
                return False
        # Binary tree has one root node. If we have more than one, then one if true
        # root node and the rest are orphan nodes.
        root_node = set(range(n)) - set(self.hsh_parent.keys())
        #print(f'potential root node = {root_node}')
        if len(root_node) != 1:
            return False
        root_node = list(root_node)[0]
        self.seen = set()
        self.isValid = True
        self.seen.add(root_node)
        dfs(root_node)
        for k in self.hsh_child:
            if k not in self.seen:
                return False
        return self.isValid

# Main section
for n, leftChild, rightChild, res in [
                                        (4, [1,-1,3,-1], [2,-1,-1,-1], True),
                                        (4, [1,-1,3,-1], [2,3,-1,-1], False),
                                        (2, [1,0], [-1,-1], False),
                                        (5, [1,3,-1,-1,-1], [2,-1,4,-1,-1], True),
                                        (4, [-1,2,3,-1], [2,-1,-1,-1], False),
                                        (4, [3,-1,1,-1], [-1,-1,0,-1], True),
                                        (4, [-1,-1,-1,-1], [-1,-1,-1,-1], False),
                                        (4, [1,-1,-1,-1], [2,-1,-1,-1], False),
                                        (1, [-1], [-1], True),
                                     ]:
    print(f'n, leftChild, rightChild = {n}, {leftChild}, {rightChild}')
    sol = Solution()
    r = sol.validateBinaryTreeNodes(n, leftChild, rightChild)
    print(f'r = {r}')
    #assert(r == res)
    print('=====================')


