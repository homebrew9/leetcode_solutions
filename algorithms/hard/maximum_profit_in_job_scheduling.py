from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # O(nlog(n))
        lst = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dpEndTime = [0]
        dpProfit = [0]
        
        for start, end, pro in lst:
            # find rightMost idx to insert this start time
            # idx is where this new start needs to be inserted
            # idx - 1 is the one that doesn't overlap
            idx = self.bSearch(dpEndTime, start)
            lastProfit = dpProfit[-1]
            currProfit = dpProfit[idx-1] + pro # they don't overlap
            # whenever we find currProfit greater than last, we update
            if currProfit > lastProfit:
                dpEndTime.append(end)
                dpProfit.append(currProfit)
        return dpProfit[-1]
    
    def bSearch(self, dp, target):
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right)//2
            if dp[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

# Main section
for startTime, endTime, profit in [
                                     ([1,2,3,3], [3,4,5,6], [50,10,40,70]),
                                     ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]),
                                     ([1,1,1], [2,3,4], [5,6,4]),
                                  ]:
    print(f'startTime, endTime, profit = {startTime}, {endTime}, {profit}')
    sol = Solution()
    r = sol.jobScheduling(startTime, endTime, profit)
    print(f'r = {r}')
    print('====================')



