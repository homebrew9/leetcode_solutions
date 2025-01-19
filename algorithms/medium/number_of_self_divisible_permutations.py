#
# The idea is good, but the algorithm is way too slow for n >= 10.
# For n = 12, it loops through 12! = 479_001_600 permutations and
# checks the gcd property for each one! Obviously that will throw TLE.
# Use backtracking and do an early exit if gcd property fails.
#

class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        def is_self_divisible(nums):
            for i, v in enumerate(nums):
                if gcd(v, i+1) != 1:
                    return False
            return True
        def next_permutation(nums):
            # Narayan Pandita algorithm
            # Find greatest i such that A[i] < A[i+1]
            # Find greatest j, where j > i, such that A[j] > A[i]
            # Swap A[i] and A[j]
            # Reverse A[i+1]...A[N-1]
            # Return false if we are at the last permutation
            N = len(nums)
            i = N - 2
            while i >= 0 and nums[i] >= nums[i+1]:
                i -= 1
            if i < 0:
                return (nums, False)
            j = N - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            p, q = i + 1, N - 1
            while p < q:
                nums[p], nums[q] = nums[q], nums[p]
                p, q = p + 1, q - 1
            return (nums, True)
        nums = [i for i in range(1, n+1)]
        res = 0
        while True:
            if is_self_divisible(nums):
                res += 1
            nums, valid = next_permutation(nums)
            if not valid:
                break
            #print(nums)
        return res

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            #11,
            #12,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.selfDivisiblePermutationCount(n)
    print(f'r = {r}')
    print('==============')


