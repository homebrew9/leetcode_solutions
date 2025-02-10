class Solution:
    def clearDigits(self, s: str) -> str:
        res = ''
        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                res = s[i] + res
        return res

# Main section
for s in [
            'abc',
            'cb34',
            'xxxl5tvjgwfwq6phngngqwb3nowq55zox3ahwpeky667aukemg3j9z6mrli0cdwden5khp91aqlard9w3h8es01gqbdgg2m3i9o1',

         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.clearDigits(s)
    print(f'r = {r}')
    print('============================')

