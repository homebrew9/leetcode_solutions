from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def maxRequest(index, count):
            print(f'\tindex, count, indegree = {index}, {count}, {indegree}')
            if index == len(requests):
                print(f'\t\tinside if index == len...')
                # Check if all buildings have an in-degree of 0
                for i in range(n):
                    if indegree[i] != 0:
                        return
                self.answer = max(self.answer, count)
                print(f'\t\t\tanswer = {self.answer}')
                return

            # Consider this request, increment and decrement for the buildings involved
            indegree[requests[index][0]] -= 1
            indegree[requests[index][1]] += 1
            # Move on to the next request and also incement the count of requests
            maxRequest(index+1, count+1)
            # Backtrack to the previous values to move back to the original state before
            # the second recursion
            indegree[requests[index][0]] += 1
            indegree[requests[index][1]] -= 1
            
            # Ignore this request and move on to the next request without incrementing the count
            maxRequest(index+1, count)
            
        self.answer = 0
        indegree = [0 for _ in range(n)]
        maxRequest(0, 0)
        return self.answer

# Main section
for n, requests in [
                      #(5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]),
                      (3, [[0,0],[1,2],[2,1]]),
                      #(4, [[0,3],[3,1],[1,2],[2,0]]),
                   ]:
    print(f'n, requests = {n}, {requests}')
    sol = Solution()
    r = sol.maximumRequests(n, requests)
    print(f'r = {r}')
    print('===================')

