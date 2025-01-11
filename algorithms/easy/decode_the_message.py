class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        chars = set()
        alphabet = [chr(i) for i in range(97,123)]
        hsh = dict()
        i = 0
        for ch in key:
            if ch == ' ':
                continue
            if ch in chars:
                continue
            chars.add(ch)
            hsh[ch] = alphabet[i]
            i += 1
        hsh[' '] = ' '
        # Now decode the message
        s = ''
        for ch in message:
            s += hsh[ch]
        return s

# Main section
for key, message in [
                       ('the quick brown fox jumps over the lazy dog', 'vkbs bs t suepuv'),
                       ('eljuxhpwnyrdgtqkviszcfmabo', 'zwx hnfx lqantp mnoeius ycgk vcnjrdb'),
                       ('zyxwvutsrqponmlkjihgfedcba', 'the quick brown fox jumps over the lazy dog'),
                    ]:
    print(f'key, message = {key}, {message}')
    sol = Solution()
    r = sol.decodeMessage(key, message)
    print(f'r = {r}')
    print('==========================')

