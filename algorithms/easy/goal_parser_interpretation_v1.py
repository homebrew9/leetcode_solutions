class Solution:
    def interpret(self, command: str) -> str:
        hsh = {'G': 'G', '()': 'o', '(al)': 'al'}
        ans = ''
        curr = ''
        for ch in command:
            curr += ch
            if curr in hsh:
                ans += hsh[curr]
                curr = ''
        return ans

# Main section
for command in [
                  'G()(al)',
                  'G()()()()(al)',
                  '(al)G(al)()G',
                  '()G',
               ]:
    print(f'command = {command}')
    sol = Solution()
    r = sol.interpret(command)
    print(f'r = {r}')
    print('=================')


