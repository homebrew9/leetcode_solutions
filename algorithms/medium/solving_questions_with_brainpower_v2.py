from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        
        for i in range(n - 2, -1, -1):
            dp[i] = questions[i][0]
            skip = questions[i][1]
            if i + skip + 1 < n:
                dp[i] += dp[i + skip + 1]

            # dp[i] = max(solve it, skip it)
            dp[i] = max(dp[i], dp[i + 1])
        
        return dp[0]

# Main section
for questions in [
                    [[3,2],[4,3],[4,4],[2,5]],
                    [[1,1],[2,2],[3,3],[4,4],[5,5]],
                    [[8,4],[3,2],[6,4],[7,7],[2,7],[7,3],[3,3],[1,4],[1,10],[4,2],[2,3],[6,9],[5,10],[1,9],[6,7],[7,5],[2,1],[3,7],[5,2],[1,7]],
                 ]:
    print(f'questions = {questions}')
    sol = Solution()
    r = sol.mostPoints(questions)
    print(f'r = {r}')
    print('========================')

