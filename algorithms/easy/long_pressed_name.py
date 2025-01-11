class Solution:
    #def isLongPressedName(self, name: str, typed: str) -> bool:
    #    left, right = 0, 0
    #    i = 0
    #    while left < len(typed):
    #        if i >= len(name) or typed[left] != name[i]:
    #            return False
    #        while right < len(typed) and typed[right] == typed[left]:
    #            right += 1
    #        left = right
    #        i += 1
    #    if i < len(name):
    #        return False
    #    return True

    def isLongPressedName(self, name: str, typed: str) -> bool:
        def getCounter(s):
            arr = list()
            cnt = 1
            for i in range(1, len(s)):
                if s[i] != s[i-1]:
                    arr.append((s[i-1], cnt))
                    cnt = 1
                else:
                    cnt += 1
            arr.append((s[-1], cnt))
            return arr

        arr1 = getCounter(name)
        arr2 = getCounter(typed)
        if len(arr1) != len(arr2):
            return False
        for x, y in zip(arr1, arr2):
            if x[0] != y[0] or y[1] < x[1]:
                return False
        return True

# Main section
for name, typed in [
                      ('alex', 'aaleex'),
                      ('saeed', 'ssaaedd'),
                      ('jonathan', 'jjoonnnnnnnnath'),
                      ('jonathan', 'jjoonnnnnnnnathannnm'),
                      ('a', 'a'),
                      ('abcd', 'aabbbbc'),
                      ('abcd', 'aabbbbcd'),
                      ('abcd', 'aabbbbcddd'),
                      ('abcd', 'aabbbbcdddeeeee'),
                      ('abcd', 'pqrs'),
                      ('leelee', 'lleeelee'),
                      ('abccd', 'abbbcd'),
                   ]:
    print(f'name, typed = {name}, {typed}')
    sol = Solution()
    r = sol.isLongPressedName(name, typed)
    print(f'r = {r}')
    print('====================')

