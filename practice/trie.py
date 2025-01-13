#
# Creating a Trie structure to store words of a dictionary.
#
class TrieNode:
    def __init__(self, ch=''):
        self.char = ch
        self.children = dict()
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                new_node = TrieNode(ch)
                node.children[ch] = new_node
                node = new_node
        node.is_end = True
    def search(self, word):
        node = self.root
        for ch in word:
            if not ch in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    def searchDFS(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            if word[i] not in node.children:
                return False
            return dfs(node.children[word[i]], i+1)
        return dfs(self.root, 0)
    def searchRegex(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            if word[i] == '.':
                for ch in node.children:
                    ret = dfs(node.children[ch], i+1)
                    if ret:
                        return True
            if word[i] not in node.children:
                return False
            return dfs(node.children[word[i]], i+1)
        return dfs(self.root, 0)

# Main section
wd = WordDictionary()
wd.insert('fad')
wd.insert('sad')
wd.insert('mad')

for word, isRegex in [
                        ('sad'  , False),
                        ('mad'  , False),
                        ('sap'  , False),
                        ('sed'  , False),
                        ('tad'  , False),
                        ('sa'   , False),
                        ('.ad'  , True),
                        ('..d'  , True),
                        ('...'  , True),
                        ('....' , True),
                        ('se.'  , True),
                        ('..p'  , True),
                        ('.a'   , True),
                        ('.e'   , True),
                        ('..'   , True),
                        ('.'    , True),
                     ]:
    print(f'word, isRegex = {word}, {isRegex}')
    r1, r2, r3 = None, None, None
    r1 = wd.search(word)
    r2 = wd.searchDFS(word)
    r3 = wd.searchRegex(word)
    print(f'r1, r2, r3 = {r1}, {r2}, {r3}')
    print('====================')


