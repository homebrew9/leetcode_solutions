from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def sign(x):
            # x will never be 0
            if x > 0:
                return 1
            elif x < 0:
                return -1
        stack = list()
        N = len(asteroids)
        currDirection = None
        for i, v in enumerate(asteroids):
            if i == 0:
                currDirection = sign(v)
                stack.append(v)
            else:
                if not stack:
                    stack.append(v)
                elif sign(v) == sign(stack[-1]):
                    stack.append(v)
                else:
                    # Directions are different.
                    # Handle the case where v is moving to left and stack[-1] to the right
                    if sign(v) == -1 and sign(stack[-1]) == 1:
                        if abs(v) == abs(stack[-1]):
                            stack.pop()
                        else:
                            while stack and sign(v) == -1 and sign(stack[-1]) == 1 and abs(v) > abs(stack[-1]):
                                stack.pop()
                            # After we've done all this popping, a couple of things can happen:
                            # stack is empty or directions are same => append to stack
                            # directions are different and magnitudes are same => pop from stack
                            if not stack:
                                stack.append(v)
                            elif sign(v) == sign(stack[-1]):
                                stack.append(v)
                            elif sign(v) == -1 and sign(stack[-1]) == 1 and abs(v) == abs(stack[-1]):
                                stack.pop()
                    else:
                        # Now v is moving to right and stack[-1] to left. Okay to append to stack.
                        stack.append(v)
        return stack

# Main section
for asteroids in [
                    [5,10,-5],
                    [8,-8],
                    [10,2,-5],
                    [1,2,3,-8,-9,-10],
                    [8,9,10,-1,-2,-3],
                    [8,9,10,-10,-10,-10],
                    [8,9,10,-10,-9,-8],
                    [8,9,10,-10,-9,-8,1,-1,2,-2,3],
                    [8,9,10,-10,-9,-8,1,-1,2,-2,3,4,5],
                    [8,9,10,-10,-9,-8,1,-1,2,-2,3,4,5,-4],
                    [8,9,10,-10,-9,-8,1,-1,2,-2,3,4,5,-6],
                    [-9,1,2,3],
                    [-1,-2,-3,1,2,3],
                    [1,2,3,-9],
                    [1,2,3,-9,10],
                    [-1,-2,-3,9,-10],
                    [-2,2,1,-2],
                 ]:
    print(f'asteroids = {asteroids}')
    sol = Solution()
    r = sol.asteroidCollision(asteroids)
    print(f'r = {r}')
    print('=====================')

