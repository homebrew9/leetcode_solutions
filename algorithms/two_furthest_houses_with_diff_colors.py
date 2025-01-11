from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        dist = 0
        left = 0
        right = len(colors) - 1
        max_dist = 0
        while True:
            if left == right:
                return dist
            if colors[left] == colors[right]:
                right -= 1
            else:
                dist = right - left

        while colors[left] == colors[right]:
            right -= 1
        dist = right - left
        if dist > max_dist:
            max_dist = dist

        left += 1

        while colors[left] == colors[right]:
            left += 1
        dist = right - left
        if dist > max_dist:
            max_dist = dist

        
