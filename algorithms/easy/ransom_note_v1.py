class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Without using collections.Counter()
        hsh = dict()
        for ch in magazine:
            hsh[ch] = hsh.get(ch,0) + 1
        print(hsh)
        for ch in ransomNote:
            if not ch in hsh or hsh[ch] == 0:
                return False
            hsh[ch] -= 1
        return True

# Main section
sol = Solution()
for rn, mg in [
                 ('a', 'b'),
                 ('aa', 'ab'),
                 ('aa', 'aab'),
                 ('thequickbrownfoxjumpsoverthelazydog', 'abcdeeefghhijklmnoooopqrrsttuuvwxyz'),
                 ('thequickbrownfoxjumpsoverthelazydog', 'abcdeeefghhijklmnoooopqrrsttuuvwxyzabcdefghijklmnopqrstuvwxyz'),
                 ('def', 'abc'),
                 ('aaaaa', 'aaaab'),
              ]:
    print(f'rn, mg = {rn}, {mg}')
    r = sol.canConstruct(rn, mg)
    print(f'r = {r}')
    print('===========================')


