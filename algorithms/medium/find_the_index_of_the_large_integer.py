# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        '''
            Make sure we have equal number of elements on both sides.
            If one half has more elements, then include mid for the other side.
            [7,8]
            [6,6,12]
            [6,6,6,12]
            [1,1,1,4,1]
            [3,2,2,2,2,2]
        '''
        left = 0
        right = reader.length() - 1
        #print(left, right)
        while left <= right:
            if left == right:
                return left
            mid = (left + right) // 2
            left_size = mid + 1 - left
            right_size = right - mid
            if left_size == right_size:
                val = reader.compareSub(left, mid, mid+1, right)
            elif left_size > right_size:
                val = reader.compareSub(left, mid, mid, right)
            if val == 1:
                right = mid
            elif val == -1:
                left = mid + 1
            else:
                return mid


