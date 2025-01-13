#
# Given a list of integers and a target, return the set of all combinations of
# integers in the list that add up to target. Repetitions are allowed. For example,
# if nums = [2,3,4] and target = 8 then ans = {(2,2,4), (2,2,2,2), (2,3,3), (4,4)}
# Note that backtracking via recursive calls quickly becomes expensive! Check the
# value of total calls.
#

def combinationSum(nums, target):
    def combine(totalSoFar, arr):
        global calls
        calls += 1
        if totalSoFar >= target:
            if totalSoFar == target:
                st.add(tuple(sorted(arr)))
            return
        for x in nums:
            if totalSoFar+x <= target:
                combine(totalSoFar+x, arr+[x])

    global calls
    calls = 0
    st = set()
    arr = list()
    totalSoFar = 0
    combine(totalSoFar, arr)
    print(f'==> Total calls = {calls}')
    return st

# Main section
for nums, target in [
                       ([2,3,4], 8),
                       ([2,3,4,5], 33),
                    ]:
    print(f'nums, target = {nums}, {target}')
    r = combinationSum(nums, target)
    print(f'r = {r}')
    print('===============')


