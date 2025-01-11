class TrieNode:
    def __init__(self, char = ''):
        self.char = char
        self.children = dict()
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_end
            if word[i] == '.':
                for char in node.children:
                    if dfs(node.children[char], i+1):
                        return True
            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)
            return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')

r = obj.search('pad')
print(f'r = {r}')
r = obj.search('bad')
print(f'r = {r}')
r = obj.search('.ad')
print(f'r = {r}')
r = obj.search('b..')
print(f'r = {r}')

