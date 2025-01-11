from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sscore = sorted(score, key=lambda x: x, reverse=True)
        hsh = dict([(v, i+1) for i, v in enumerate(sscore)])
        arr = list()
        for item in score:
            if hsh[item] == 1:
                arr.append('Gold Medal')
            elif hsh[item] == 2:
                arr.append('Silver Medal')
            elif hsh[item] == 3:
                arr.append('Bronze Medal')
            else:
                arr.append(str(hsh[item]))
        return arr

# Main section
for score in [
                [5,4,3,2,1],
                [10,3,8,9,4],
                [1],
                [2,1,0],
                [0,1,2],
             ]:
    print(f'score = {score}')
    sol = Solution()
    r = sol.findRelativeRanks(score)
    print(f'r = {r}')
    print('===========================')

