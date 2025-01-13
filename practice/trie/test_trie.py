

class TrieNode:
    def __init__(self, ch=None):
        self.ch = ch
        self.children = dict()
        self.is_end = False
    def print(self):
        def dfs(node):
            print(node.ch, node.children, node.is_end)
            for k in node.children:
                dfs(node.children[k])
        dfs(self)


root = TrieNode()
orig = root
for ch in 'leet':
    root.children[ch] = TrieNode(ch)
    root = root.children[ch]


def prepare_dictionary(words):
    root = TrieNode()
    orig = root
    for word in words:
        for ch in word:
            root.children[ch] = TrieNode(ch)
            root = root.children[ch]
        root.is_end = True
    orig.print()




prepare_dictionary(['leet', 'code', 'leetcode', 'le', 'cod', 'gamer'])


root.is_end = True

orig.print()




