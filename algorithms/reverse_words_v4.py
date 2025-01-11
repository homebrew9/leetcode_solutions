# =============================================
# Using Python and stacks
# =============================================
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = list()
        ret = ''
        in_word = False
        temp = ''
        for c in s:
            if c != ' ' and not in_word:
                in_word = True
                temp += c
            elif in_word:
                if c == ' ':
                    in_word = False
                    stack.append(temp)
                    temp = ''
                else:
                    temp += c
        if temp != '':
            stack.append(temp)
        while (len(stack) > 0):
            if ret == '':
                ret += stack.pop()
            else:
                ret += ' ' + stack.pop()
        return ret

# Main section
sol = Solution()
for s in [
            'the sky is blue',
            ' the sky is blue',
            '   the sky is blue',
            'the sky is blue ',
            'the sky is blue  ',
            'the sky is blue   ',
            'the     sky     is  blue',
            ' the     sky     is  blue ',
         ]:
    print(f's = [{s}]')
    r = sol.reverseWords(s)
    print(f'r = [{r}]')
    print('=====================')

