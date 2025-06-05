class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        N = len(word)
        span = N - numFriends + 1
        res = ''
        for i in range(N):
            chunk = word[i:i+span]
            res = max(res, chunk)
        return res

# Main section
for word, numFriends in [
                           ('dbca', 2),
                           ('gggg', 4),
                           ('gh', 1),
                        ]:
    print(f'word, numFriends = {word}, {numFriends}')
    sol = Solution()
    r = sol.answerString(word, numFriends)
    print(f'r = {r}')
    print('=======================')

