from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        arr = [[i+1, p, h, r] for i, (p, h, r) in enumerate(zip(positions, healths, directions))]
        arr.sort(key = lambda x: x[1])
        stack = list()
        for i, p, h, r in arr:
            if not stack:
                stack.append([i, p, h, r])
            else:
                if r == 'L':
                    if stack[-1][3] == 'R':
                        if stack[-1][2] == h:
                            stack.pop()
                        elif stack[-1][2] > h:
                            stack[-1][2] -= 1
                        else:
                            tmp = h
                            while stack and stack[-1][3] == 'R' and stack[-1][2] < tmp:
                                tmp -= 1
                                stack.pop()
                            if stack and stack[-1][3] == 'R':
                                if stack[-1][2] > tmp:
                                    stack[-1][2] -= 1
                                else:
                                    stack.pop()
                            else:
                                stack.append([i, p, tmp, r])
                    else:
                        stack.append([i, p, h, r])
                else:
                    stack.append([i, p, h, r])
        return [h for i, p, h, r in sorted(stack, key=lambda x: x[0])]

# Main section
for positions, healths, directions in [
        ([675,163,166,682,696,701,190,189,192,199], [876,948,767,82,702,666,888,264,232,994], 'LLRLRRRRLL'),
        ([5,17,529,20,23,35,46,560,564,567,55,570,571,62,584,585,77,91,101,613,109,628,631,125,642,134,144,657,668,161,675,163,166,682,696,701,190,189,192,199], [623,52,751,922,28,469,334,362,793,54,814,484,798,70,880,822,751,624,161,221,468,625,964,901,136,110,120,850,132,636,876,948,767,82,702,666,888,264,232,994], 'LLRRLRLRRRRLLRLRRLLLLLLRLLLRLRLLRLRRRRLL'),
        ([5,17,529,20,23,35,46,560,564,567,55,570,571,62,584,585,77,91,101,613,109,628,631,125,642,134,144,657,668,161,675,163,166,682,696,701,190,189,192,199,711,714,718,215,218,738,741,742,744,749,757,254,258,782,281,803,811,313,836,838,342,346,858,347,869,872,877,879,368,886,383,895,393,394,911,913,405,920,409,938,430,948,436,965,970,971,458,473,474,989,991,999,498,510,511], [623,52,751,922,28,469,334,362,793,54,814,484,798,70,880,822,751,624,161,221,468,625,964,901,136,110,120,850,132,636,876,948,767,82,702,666,888,264,232,994,917,328,596,929,546,744,177,726,326,196,646,15,390,52,558,364,160,145,838,379,753,91,174,671,992,439,75,458,827,329,347,113,492,688,261,655,16,978,375,548,5,407,189,833,482,156,707,733,513,397,445,602,902,596,541], 'LLRRLRLRRRRLLRLRRLLLLLLRLLLRLRLLRLRRRRLLRLLRRLLRLLRRLRLLRLLLRRRRLRRRRLRRLRLRRRRRLRRLLLRRLRLLRLR'),
        ([5,4,3,2,1], [2,17,9,15,10], 'RRRRR'),
        ([3,5,2,6], [10,10,15,12], 'RLRL'),
        ([1,2,5,6], [10,10,11,11], 'RLRL'),
        ([5,17,529,20,23,35,46,560,564,567,55,570,571,62,584,585,77,91,101,613,109,628,631,125,642,134,144,657,668,161,675,163,166,682,696,701,190,189,192,199,711,714,718,215,218,738,741,742,744,749,757,254,258,782,281,803,811,313,836,838,342,346,858,347,869,872,877,879,368,886,383,895,393,394,911,913,405,920,409,938,430,948,436,965,970,971,458,473,474,989,991,999,498,510,511], [623,52,751,922,28,469,334,362,793,54,814,484,798,70,880,822,751,624,161,221,468,625,964,901,136,110,120,850,132,636,876,948,767,82,702,666,888,264,232,994,917,328,596,929,546,744,177,726,326,196,646,15,390,52,558,364,160,145,838,379,753,91,174,671,992,439,75,458,827,329,347,113,492,688,261,655,16,978,375,548,5,407,189,833,482,156,707,733,513,397,445,602,902,596,541], 'LLRRLRLRRRRLLRLRRLLLLLLRLLLRLRLLRLRRRRLLRLLRRLLRLLRRLRLLRLLLRRRRLRRRRLRRLRLRRRRRLRRLLLRRLRLLRLR'),
    ]:
    print(f'positions  = {positions}')
    print(f'healths    = {healths}')
    print(f'directions = {directions}')
    sol = Solution()
    r = sol.survivedRobotsHealths(positions, healths, directions)
    print(f'r = {r}')
    print('===================')


