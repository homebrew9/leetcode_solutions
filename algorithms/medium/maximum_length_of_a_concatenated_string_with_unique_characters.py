from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_len = 0
        def genSubsequences(arr, index, subarr):
            if index == len(arr):
                #print(f'\tsubarr = {subarr}')
                if len(set(''.join(subarr))) == len(''.join(subarr)):
                    #print(f'\tsubarr = {subarr}')
                    self.max_len = max(self.max_len, len(''.join(subarr)))
            else:
                genSubsequences(arr, index+1, subarr)
                genSubsequences(arr, index+1, subarr+[arr[index]])
            return
        genSubsequences(arr, 0, [])
        return self.max_len

# Main section
for arr in [
              #['un','iq','ue'],
              #['cha','r','act','ers'],
              #['abcdefghijklmnopqrstuvwxyz'],
              #['ab','cd','ef'],
              #['a','a','a'],
              #['th','eq','ui','ck','br','own','fo','xju','mp','so','ve','rt','hel','az','y','dog'],
              #['aba','bcb','cdc','ded','efe'],
              ['abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz'],
              ['uu','iq','ue'],
              ['un','iq','ue'],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.maxLength(arr)
    print(f'r = {r}')
    print('=================')

