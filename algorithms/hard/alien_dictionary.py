from typing import List
from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def compare_words(s, t):
            # It is *VERY IMPORTANT* to understand why we break after the first comparison of distinct characters!
            # Let's say the two words are: ["aaaze", "aaayf"]
            # The first three characters are the same in both: "aaa", so we cannot compare them.
            # The next comparison is "z" <-> "y". Here "z" appears before "y".
            # But now when we come to the next set: "e" <-> "f", we cannot say that "e" appears before "f".
            # In this alien dictionary, "e" can be before or after "f".
            # As an analogy, notice how comparison is done in regular English: "amount" < "argument"
            # After the first character is compared, we skip the rest of each word.
            # 1) "amount" | "argument" => Skip 'a', then 'm' < 'r' hence 'amount' < 'argument'. Note that 'o' > 'g'
            # 2) "amend"  | "argument" => Skip 'a', then 'm' < 'r' hence 'amend'  < 'argument'. Note that 'e' < 'g'
            # 3) "amgen"  | "argument" => Skip 'a', then 'm' < 'r' hence 'amgen'  < 'argument'. Note that 'g' = 'g'
            #print(f'\ts, t = {s}, {t}')
            was_compared = False
            for a, b in zip(s, t):
                if a != b:
                    was_compared = True
                    children[a] += [b]
                    indegree[b] += 1
                    break
            if not was_compared:
                if s.startswith(t) and len(s) > len(t):
                    return False
            return True
        N = len(words)
        children = defaultdict(list)
        char_set = set(''.join(words))
        indegree = defaultdict(int, {w: 0 for w in char_set})
        for i in range(1, N):
            is_valid = compare_words(words[i-1], words[i])
            if not is_valid:
                return ''
        #print(children)
        #print(indegree)
        # Kahn's Topological Sorting algorithm
        dq = deque([k for k, v in indegree.items() if v == 0])
        #print(dq)
        res = list()
        while dq:
            #print(f'\tdq, indegree, res = {dq}, {indegree}, {res}')
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                res.append(curr)
                for child in children[curr]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        dq.append(child)
        #print(f'res = {res}')
        return ''.join(res) if len(res) == len(char_set) else ''

# Main section
for words in [
                ['wrt','wrf','er','ett','rftt'],
                ['z','x'],
                ['z','x','z'],
                ['wrt','wrf','er','ett','rftt','te'],
                ['z','z'],
                ['abc','ab'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.alienOrder(words)
    print(f'r = {r}')
    print('=====================')

