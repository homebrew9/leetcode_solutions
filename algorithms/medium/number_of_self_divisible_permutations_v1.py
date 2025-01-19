#
# The idea is good, but the algorithm is way too slow for n >= 10.
# For n = 12, it loops through 12! = 479_001_600 permutations and
# checks the gcd property for each one! Obviously that will throw TLE.
# Use backtracking and do an early exit if gcd property fails.
# Not sure why this doesn't work!!
#

class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        #
        # The array [1,2,3] has 3 self-divisble permutations: [1,3,2], [2,3,1], [3,1,2]
        #
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        def is_self_divisible(nums):
            for i, v in enumerate(nums):
                if gcd(v, i+1) != 1:
                    return False
            return True
        def search(permutation, chosen, indent):
            print(f'{">>" * indent}search({permutation}, {chosen})')
            if len(permutation) == n:
                print(permutation)
                return
            for i in range(n):
                if chosen[i]:
                    continue
                chosen[i] = True
                print(f'{">>" * indent}gcd: gcd({len(permutation)+1}, {nums[i]}) = {gcd(len(permutation)+1, nums[i])}')
                if gcd(len(permutation)+1, nums[i]) != 1:
                    print(f'{">>" * indent}gcd != 1, returning...')
                    return
                permutation.append(nums[i])
                search(permutation, chosen, indent+1)
                chosen[i] = False
                permutation.pop()
        nums = [i for i in range(1, n+1)]
        print(nums)
        chosen = [False for i in range(1, n+1)]
        permutation = list()
        res = 0
        search(permutation, chosen, 1)
        return res

# Main section
for n in [
            #1,
            #2,
            3,
            #4,
            #5,
            #6,
            #7,
            #8,
            #9,
            #10,
            #11,
            #12,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.selfDivisiblePermutationCount(n)
    print(f'r = {r}')
    print('==============')



