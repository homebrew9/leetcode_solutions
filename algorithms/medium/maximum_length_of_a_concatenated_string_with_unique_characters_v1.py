#
# I have tried to use DP over here. The set "self.st" contains all the index tuples
# that duplicate characters. We do an early exit if the index tuple is in the set.
# For example: arr = ['uu','iq','ue'] here index 0 has duplicate characters so
# self.st = {(0,)} and we do not generate subsequences: (0,1), (0,2)
# In the example: arr = ['un','iq','ue'], the index tuple (0,2) has duplicate chars
# so it is stored in the set and the subsequences (0,2) and (0,1,2) are not generated.
# 
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_len = 0
        self.st = set()
        def genSubsequences(arr, index, subarr, ind_tuple):
            #print(f'index, self.st, ind_tuple, subarr = {index}, {self.st}, {ind_tuple}, {subarr}')
            if ind_tuple in self.st:
                return
            if index < len(arr) and len(set(arr[index])) != len(arr[index]):
                self.st.add((index,))
            if len(set(''.join(subarr))) != len(''.join(subarr)):
                self.st.add(ind_tuple)
                return
            if index == len(arr):
                print(f'\tsubarr = {subarr}')
                #if len(set(''.join(subarr))) == len(''.join(subarr)):
                #    #print(f'\tarr = {subarr}')
                #    self.max_len = max(self.max_len, len(''.join(subarr)))
                self.max_len = max(self.max_len, len(''.join(subarr)))
            else:
                genSubsequences(arr, index+1, subarr, ind_tuple)
                if not (index) in self.st and not ind_tuple+(index,) in self.st:
                    genSubsequences(arr, index+1, subarr+[arr[index]], ind_tuple+(index,))
            return
        genSubsequences(arr, 0, [], ())
        print(f'self.st = {self.st}')
        return self.max_len

# Main section
for arr in [
              ['un','iq','ue'],
              ['cha','r','act','ers'],
              ['abcdefghijklmnopqrstuvwxyz'],
              ['ab','cd','ef'],
              ['a','a','a'],
              ['th','eq','ui','ck','br','own','fo','xju','mp','so','ve','rt','hel','az','y','dog'],
              ['aba','bcb','cdc','ded','efe'],
              ['abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz'],
              ['uu','iq','ue'],
              ['un','iq','ue'],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.maxLength(arr)
    print(f'r = {r}')
    print('=================')

