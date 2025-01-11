class Solution:
    def interpret(self, command: str) -> str:
        hsh = {'G': 'G', '()': 'o', '(al)': 'al'}
        i = 0
        ans = ''
        while True:
            if i >= len(command):
                break
            if command[i] == 'G':
                ans += hsh['G']
                i += 1
            elif command[i:i+2] == '()':
                ans += hsh['()']
                i += 2
            elif command[i:i+4] == '(al)':
                ans += hsh['(al)']
                i += 4
            print(f'\ti, ans = {i}, {ans}')
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

