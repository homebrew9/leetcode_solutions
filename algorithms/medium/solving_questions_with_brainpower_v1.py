from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def solve(i):
            if i >= N:
                return 0
            if i in memo:
                return memo[i]
            points, brainpower = questions[i]
            memo[i] = max(points + solve(i + brainpower + 1), solve(i + 1))
            return memo[i]
        N = len(questions)
        memo = dict()
        return solve(0)

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

