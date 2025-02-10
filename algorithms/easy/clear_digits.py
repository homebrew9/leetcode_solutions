class Solution:
    def clearDigits(self, s: str) -> str:
        stack = list()
        for ch in s:
            if ch.isdigit():
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

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

