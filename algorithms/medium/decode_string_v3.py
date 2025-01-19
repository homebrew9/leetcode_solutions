#
# Doesn't work... something wrong with the logic
#
class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        in_num, num_token = False, ''
        in_str, str_token = False, ''
        for ch in s:
            print(f'ch = {ch}, num_token = [{num_token}], str_token = [{str_token}], stack = {stack}')
            if ch.isdigit():
                if in_str:
                    stack.append(str_token)
                    str_token = ''
                    in_str = False
                in_num = True
                num_token += ch
            elif ch.isalpha():
                in_str = True
                str_token += ch
            elif ch == '[':
                stack.append(num_token)
                num_token = ''
                in_num = False
            elif ch == ']':
                if len(str_token) > 0:
                    chunk = str_token
                    while stack and stack[-1].isalpha():
                        chunk = stack.pop() + chunk
                    while stack and stack[-1].isdigit():
                        times = int(stack.pop())
                        chunk = chunk * times
                    stack.append(chunk)
                    in_str = False
                    str_token = ''
                else:
                    chunk = ''
                    while stack and stack[-1].isalpha():
                        chunk = stack.pop() + chunk
                    while stack and stack[-1].isdigit():
                        times = int(stack.pop())
                        chunk = chunk * times
                    stack.append(chunk)
                    in_str = False
                    str_token = ''
        chunk = str_token
        while stack and stack[-1].isalpha():
            chunk = stack.pop() + chunk
        while stack and stack[-1].isdigit():
            times = int(stack.pop())
            chunk = chunk * times
        stack.append(chunk)
        return ''.join(stack)


"3[a]2[bc]"
"3[a2[c]]"
"2[abc]3[cd]ef"
"2[2[2[bc]x]]"     <==========
"2[3[4[abc]xyz]]"
"abc2[3[4[abc]xyz]]"
"abc2[3[4[abc]xyz]]mno"
"a"
"abc"
"abc4[xyz5[pqr6[def]ghi]jkl]mno"

