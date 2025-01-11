class TrieNode:
    def __init__(self, char = ''):
        self.char = char
        self.children = dict()
        self.is_end = False

class Trie:
    def __init__(self):
        # Initialize your data structure here.
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Inserts a word into the trie.
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
        # Returns if the word is in the trie.
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        # Reached at the end of word
        # return True if word is present, i.e is_end = True else False
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        # Returns if there is any word in the trie that starts with the given prefix.
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert('le')
obj.insert('leet')
obj.insert('code')
r = obj.search('leet')
print(f'r = {r}')
r = obj.search('cod')
print(f'r = {r}')
r = obj.startsWith('co')
print(f'r = {r}')

