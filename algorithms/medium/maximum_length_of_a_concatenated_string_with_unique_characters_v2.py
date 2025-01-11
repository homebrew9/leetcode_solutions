# Think in terms of graph.
# INPUT: ["cha", "r", "act", "ers"]
# 
# Make a graph for paths starting from each word in input
# 
# 1.             "cha"
#               /  |  \
#              "r" "act" "ers"
#              /\     \
#         "act" "ers" "ers"
#         
#         PATHS (sub-sequences): 
#         cha            - No Duplicates OK : max_len = 3
#         cha-r          - No Duplicates OK: max_len = 4
#         cha-r-act      - Duplicate char 'a' NOTOK
#         cha-r-ers      - Duplicate char 'r' NOTOK
#         cha-act        - Duplicate char 'a' NOTOK
#         cha-act-ers    - Duplicate char 'a','c' NOTOK
#         cha-ers        - No Duplicates OK: max_len = 6
# 
# Similarly for other paths starting with "r", "act", "ers"
# 
# 2.            "r"
#              /  \
#           "act"   "ers"
#           /
#           "ers"
# 
# 3.        "act"
#             |
#           "ers"
# 
# 4.        "ers"
#          
# So, basically you just have to dfs on all words and treat them as starting word of a subsequence.
#
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max_len = 0
        def dfs(arr, curr_subseq, idx):
            #print(f'\tcurr_subseq, idx = {curr_subseq}, {idx}')
            # Return if duplicate characters
            if len(curr_subseq) != len(set(curr_subseq)):
                return
            # Update max_len if curr_subseq is maximal
            self.max_len = max(len(curr_subseq), self.max_len)
            # dfs on next subseq(s) starting from curr_subseq
            for i in range(idx, len(arr)):
                dfs(arr, curr_subseq + arr[i], i+1)

        dfs(arr, '', 0)
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

