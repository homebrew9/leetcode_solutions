from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_counter = Counter(ransomNote)
        mg_counter = Counter(magazine)
        for k in rn_counter:
            if not (k in mg_counter and mg_counter[k] >= rn_counter[k]):
                return False
        return True

# Main section
sol = Solution()
for rn, mg in [
                 ('a', 'b'),
                 ('aa', 'ab'),
                 ('aa', 'aab'),
                 ('thequickbrownfoxjumpsoverthelazydog', 'abcdeeefghhijklmnoooopqrrsttuuvwxyz'),
                 ('thequickbrownfoxjumpsoverthelazydog', 'abcdeeefghhijklmnoooopqrrsttuuvwxyzabcdefghijklmnopqrstuvwxyz'),
              ]:
    print(f'rn, mg = {rn}, {mg}')
    r = sol.canConstruct(rn, mg)
    print(f'r = {r}')
    print('===========================')

