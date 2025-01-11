from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        lookup = set(words)
        print(f'\tlookup = {lookup}')

        # O(L^2) time
        # O(L) space
        def is_good(word):
            L = len(word)
            dp = [False] * (L + 1)

            lookup.remove(word)

            dp[0] = True
            print(f'\t\tlookup, dp = {lookup}, {dp}')
            for i in range(L):
                print(f'\t\t\ti, word[i] = {i}, {word[i]}')
                if dp[i]:
                    for j in range(i, L):
                        print(f'\t\t\t\tj, word[j], word[i:j+1] = {j}, {word[j]}, {word[i:j+1]}')
                        if word[i:j + 1] in lookup:
                            dp[j + 1] |= dp[i]
                        print(f'\t\t\t\t\tdp = {dp}')
            lookup.add(word)
            return dp[L]

        # O(N * L^2) time
        # O(L + H) space where H is the size of output
        ans = []
        for word in words:
            if is_good(word):
                ans.append(word)
        return ans

# Main section
for words in [
                #['cat','cats','catsdogcats','dog','dogcatsdog','hippopotamuses','rat','ratcatdogcat'],
                #['cat','dog','catdog'],
                #['ab','cd', 'abcd'],
                ['abcd', 'ab','cd'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.findAllConcatenatedWordsInADict(words)
    print(f'r = {r}')
    print('================')

