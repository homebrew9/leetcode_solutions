from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):
            print(f'\tleft = {left} ; length_ = {length_} ; possible_dups = {possible_dups}')
            # Stop when left points beyond hte last eleement in the
            # original list which would be part of modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: this 0 can't be duplicated, we have no more space,
                # as left is pointing to the last element which could be included
                if left == length_ - possible_dups:
                    print(f'\tin edge case...')
                    arr[length_] = 0 # For this zero, we just copy it without duplication
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be
        # part of new list
        last = length_ - possible_dups
        print(f'\tlast = {last}')

        # Copy zero twice, and non-zero once
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]

        print(f'arr = {arr}')

# Main section
for arr in [
              [1,0,2,3,0,4,5,0],
              [1,0,2,3,0,0,5,0],
              [1,2,3],
              [1,2,0],
              [0],
              [9],
              [0,0],
              [0,0,0],
              [0,0,0,0],
              [0,0,0,0,0],
              [0,1,0,2,3],
              [0,1,2,3,4],
              [1,2,3,4,0],
              [1,2,0,4,5],
              [0,1,7,6,0,2,0,7],
              [0,1,7,6,9,2,7,0],
              [9,9,9,4,8,0,0,3,7,2,0,0,0,0,9,1,0,0,1,1,0,5,6,3,1,6,0,0,2,3,4,7,0,3,9,3,6,5,8,9,1,1,3,2,0,0,7,3,3,0,5,7,0,8,1,9,6,3,0,8,8,8,8,0,0,5,0,0,0,3,7,7,7,7,5,1,0,0,8,0,0],
              [9,9,9,4,8,0,0,3,7,2,0,0,0,0,9,1,0,0],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.duplicateZeros(arr)
    #print(f'r = {r}')
    print('===================')


