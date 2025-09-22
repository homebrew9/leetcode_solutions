from typing import List
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        hsh = dict()
        arr = sorted(zip(username, website, timestamp), key=lambda x: x[2])
        for u, w, _ in arr:
            if u in hsh:
                hsh[u] += [w]
            else:
                hsh[u] = [w]
        for k in hsh:
            hsh[k] = set(combinations(hsh[k], 3))
        res = tuple()
        max_score = 0
        sorted_website = [w for _, w, _ in arr]
        for tpl in combinations(sorted_website, 3):
            curr = 0
            for v in hsh.values():
                if tpl in v:
                    curr += 1
            if curr > max_score:
                max_score = curr
                res = tpl
            elif curr == max_score:
                res = min(res, tpl)
        return list(res)

# Main section
for username, timestamp, website in [
        (['joe','joe','joe','james','james','james','james','mary','mary','mary'], [1,2,3,4,5,6,7,8,9,10], ['home','about','career','home','cart','maps','home','home','about','career']),
        (['ua','ua','ua','ub','ub','ub'], [1,2,3,4,5,6], ['a','b','a','a','b','c']),
        (['lpgbr','by','by','lpgbr','by','ditctqnahs','by'], [117853717,760542754,858167998,235286033,992196098,273717872,792447849], ['inc','inc','inc','ftd','inc','ftd','inc']),
        (['zkiikgv','zkiikgv','zkiikgv','zkiikgv'], [436363475,710406388,386655081,797150921], ['wnaaxbfhxp','mryxsjc','oz','wlarkzzqht']),
        (['h','eiy','cq','h','cq','txldsscx','cq','txldsscx','h','cq','cq'], [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930], ['hibympufi','hibympufi','hibympufi','hibympufi','hibympufi','hibympufi','hibympufi','hibympufi','yljmntrclw','hibympufi','yljmntrclw']),
    ]:
    print(f'username  = {username}')
    print(f'timestamp = {timestamp}')
    print(f'website   = {website}')
    sol = Solution()
    r = sol.mostVisitedPattern(username, timestamp, website)
    print(f'r = {r}')
    print('===================')

