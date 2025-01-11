# 1095. Find in Mountain Array
# Hard
# 
# (This problem is an interactive problem.)
# 
# You may recall that an array arr is a mountain array if and only if:
# 
#     arr.length >= 3
#     There exists some i with 0 < i < arr.length - 1 such that:
#         arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#         arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.
# 
# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:
# 
#     MountainArray.get(k) returns the element of the array at index k (0-indexed).
#     MountainArray.length() returns the length of the array.
# 
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
# 
#  
# 
# Example 1:
# 
# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# 
# Example 2:
# 
# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.
# 
#  
# 
# Constraints:
# 
#     3 <= mountain_arr.length() <= 10^4
#     0 <= target <= 10^9
#     0 <= mountain_arr.get(index) <= 10^9
# 
# 
# 
# array = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]  0, 16
# array = [1,2,3,4,5,6,7,8,9,8,7,6]            0, 11
# array = [7,8,9,8,7,6,5,4,3,2,1]              0, 10
# 



# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        left, right = 0, N - 1
        peak = None
        while left < right:
            mid = (left + right) // 2
            print(left, right, mid)
            prev_val, val, next_val = mountain_arr.get(mid-1), mountain_arr.get(mid), mountain_arr.get(mid+1)
            if prev_val < val > next_val:
                # We found the peak
                peak = mid
                break
            elif prev_val < val < next_val:
                left = mid + 1
            elif prev_val > val > next_val:
                right = mid - 1
        print(f'peak = {peak}')
        ## Check on the left side of peak first
        #left, right = 0, peak
        #while left < right:
        #    mid = (left + right) // 2
        #    val = mountain_arr.get(mid)
        #    if val == target:
        #        return mid
        #    elif val > target:
        #        right = mid - 1
        #    else:
        #        left = mid + 1
        ## If we are here, then the value is not on the left side of peak.
        ## Try the right side of peak.
        #left, right = peak, N
        #while left < right:
        #    mid = (left + right) // 2
        #    val = mountain_arr.get(mid)
        #    if val == target:
        #        return mid
        #    elif val > target:
        #        right = mid - 1
        #    else:
        #        left = mid + 1
        ## target is nowhere to be found; return -1
        #return -1


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        left, right = 0, N - 1
        peak = None
        while left < right:
            mid = (left + right) // 2
            print(left, right, mid)
            prev_val, val, next_val = mountain_arr.get(mid-1), mountain_arr.get(mid), mountain_arr.get(mid+1)
            if prev_val < val > next_val:
                # We found the peak
                peak = mid
                break
            elif prev_val < val < next_val:
                left = mid
            elif prev_val > val > next_val:
                right = mid - 1
        print(f'peak = {peak}')
        print('=====')
        # Check on the left side of peak first
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                right = mid
            else:
                left = mid + 1
        print('=====')
        # If we are here, then the value is not on the left side of peak.
        # Try the right side of peak.
        left, right = peak, N
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            val = mountain_arr.get(mid)
            if val == target:
                return mid
            elif val > target:
                left = mid
            else:
                right = mid - 1
        # target is nowhere to be found; return -1
        return -1



[1,2,3,4,5,3,1]
3
[0,1,2,4,2,1]
3
[0,4,5,7,10,20,25,26,28,30,31,35,36,43,49,50,51,52,55,60,61,64,70,71,72,78,96,100,99,98,95,86,82,80,79,72,64,61,59,57,53,52,46,44,41,35,32,26,25,21,20,6,5,3,1,0]
6
[0,4,5,7,10,20,25,26,28,30,31,35,36,43,49,50,51,52,55,60,61,64,70,71,72,78,96,100,99,98,95,86,82,80,79,72,64,61,59,57,53,52,46,44,41,35,32,26,25,21,20,6,5,3,1,0]
7

# Didn't work for the following! Goes in an infinite loop!

[0,4,5,7,10,20,25,26,28,30,31,35,36,43,49,50,51,52,55,60,61,64,70,71,72,78,96,100,99,98,95,86,82,80,79,72,64,61,59,57,53,52,46,44,41,35,32,26,25,21,20,6,5]
7




