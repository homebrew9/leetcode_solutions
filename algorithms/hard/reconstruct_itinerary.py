from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Eulerian Path problem
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        itinerary = []
        dfs("JFK")
        return itinerary[::-1]

# Main section
for tickets in [
                  [['MUC','LHR'],['JFK','MUC'],['SFO','SJC'],['LHR','SFO']],
                  [['JFK','SFO'],['JFK','ATL'],['SFO','ATL'],['ATL','JFK'],['ATL','SFO']],
               ]:
    print(f'tickets = {tickets}')
    sol = Solution()
    r = sol.findItinerary(tickets)
    print(f'r = {r}')
    print('=====================')










































