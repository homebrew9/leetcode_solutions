from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        def topTwoIndexes(arr):
            highestInd = 0
            highestVal = arr[0]
            secondHighestInd = None
            secondHighestVal = float('-inf')
            for i in range(1, len(arr)):
                if arr[i] > highestVal:
                    secondHighestVal = highestVal
                    secondHighestInd = highestInd
                    highestVal = arr[i]
                    highestInd = i
                elif arr[i] > secondHighestVal:
                    secondHighestVal = arr[i]
                    secondHighestInd = i
            return (highestInd, secondHighestInd)

        seconds = 0
        while sum(amount) > 0:
            one, two = topTwoIndexes(amount)
            if amount[one] > 0:
                amount[one] -= 1
            if amount[two] > 0:
                amount[two] -= 1
            seconds += 1
        return seconds

# Main section
for amount in [
                 [1,4,2],
                 [5,4,4],
                 [5,0,0],
                 [100,100,100],
                 [73,99,23],
                 [21,51,91],
                 [91,51,21],
                 [0,0,0],
                 [67,3,89],
              ]:
    print(f'amount = {amount}')
    sol = Solution()
    r = sol.fillCups(amount)
    print(f'r = {r}')
    print('=======================')

