from typing import List

class Trie:
    def __init__(self, ch='', hsh=dict(), end=False):
        self.ch = ch
        self.hsh = hsh
        self.end = end
    def print_hierarchy(self):
        def dfs(node, i):
            print("%s -> id = %s, ch = '%s', hsh_keys = %s, end = %s"%(' '*2*i, id(node), node.ch, node.hsh.keys(), node.end))
            if len(node.hsh) == 0:
                return
            for k in node.hsh:
                dfs(node.hsh[k], i+1)
        dfs(self, 1)

class Solution:
    def longestWord(self, words: List[str]) -> str:
        def dfs(s, node):
            if not node.end:
                self.res += [s[:-1]]
                return
            if len(node.hsh) == 0:
                self.res += [s]
                return
            for k in node.hsh:
                dfs(s + k, node.hsh[k])
        # 1) Store the words in a Trie structure
        root = Trie('', dict(), False)
        #root.print_hierarchy()
        for word in words:
            curr = root
            for ch in word:
                if ch in curr.hsh:
                    curr = curr.hsh[ch]
                else:
                    new_node = Trie(ch, dict(), False)
                    curr.hsh[ch] = new_node
                    curr = new_node
            curr.end = True
        #root.print_hierarchy()
        # 2) Iterate through the Trie structure and return a list
        #    of words that were formed by other words one character
        #    at a time
        self.res = list()
        s = ''
        for k in root.hsh:
            dfs(s + k, root.hsh[k])
        #print(f'self.res = {self.res}')
        if len(self.res) == 0:
            return ''
        return sorted(self.res, key=lambda x: (-len(x), x))[0]

# Main section
for words in [
                ['w','wo','wor','worl','world'],
                ['a','banana','app','appl','ap','apply','apple'],
                ['m','mo','moc','moch','mocha','l','la','lat','latt','latte','c','ca','cat'],
                ['cap', 'cape', 'caper', 'am', 'amble', 'ambulator'],
                ['win','won','wonder','wonderland','wisdom'],
                ['a','ab','abc','abcd','abcde','abcdef','abce','abcef','abcefg','abceff','abcddf'],
                ['ogz','eyj','e','ey','hmn','v','hm','ogznkb','ogzn','hmnm','eyjuo','vuq','ogznk','og','eyjuoi','d'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.longestWord(words)
    print(f'r = {r}')
    print('=======================')



