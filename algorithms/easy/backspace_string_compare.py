class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        lst1, lst2 = [], []
        for ch in s:
            if ch == '#':
                if len(lst1) > 0:
                    lst1.pop()
            else:
                lst1.append(ch)
        for ch in t:
            if ch == '#':
                if len(lst2) > 0:
                    lst2.pop()
            else:
                lst2.append(ch)
        return lst1 == lst2

# Main section
for s, t in [
               ('ab#c', 'ad#c'),
               ('ab##', 'c#d#'),
               ('a#c', 'b'),
               ('a######', '####'),
               ('a###b###x', '####x'),
            ]:
    print(f's = {s} ; t = {t}')
    sol = Solution()
    r = sol.backspaceCompare(s, t)
    print(f'r = {r}')
    print('==========================')

