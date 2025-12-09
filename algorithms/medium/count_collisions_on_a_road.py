class Solution:
    def countCollisions(self, directions: str) -> int:
        N = len(directions)
        stack = list()
        res = 0
        for d in directions:
            if d == 'S':
                cnt = 0
                while stack and stack[-1] == 'R':
                    stack.pop()
                    cnt += 1
                    res += 1
                for _ in range(cnt+1):
                    stack.append('S')
            elif d == 'L':
                if stack:
                    if stack[-1] == 'R':
                        cnt = 0
                        first_collision = True
                        while stack and stack[-1] == 'R':
                            stack.pop()
                            cnt += 1
                            if first_collision:
                                res += 2
                                first_collision = False
                            else:
                                res += 1
                        for _ in range(cnt+1):
                            stack.append('S')
                    elif stack[-1] == 'S':
                        res += 1
                        stack.append('S')
                    else:
                        stack.append(d)
                else:
                    stack.append(d)
            elif d == 'R':
                stack.append(d)
        return res

    def countCollisions_1(self, directions: str) -> int:
        # Cars running L on the left edge will never hit anything.
        # Remove them. Cars running R on the right edge will never
        # hit anything. Remove them too.
        # So we are then left with a string, maybe like this: 'RRLLSLRRLL'
        # Note that the rightmost car will NOT be R, and leftmost will NOT be L.
        # RL = 2 collisions and both will become S.
        # Then each SL = RS = 1 collision, and each L or R becomes S.
        # By itself, S will not contribute to the total. But the R or L car hitting
        # it, will contribute. So we can remove all S cars now. The length of the
        # remaining string is the answer. Basically, we find all non-S characters.
        # 'RRLLSLRRLL' => remove S: 'RRLLLRRLL' => len = 9 = answer.
        return len(directions.lstrip('L').rstrip('R').replace('S',''))

# Main section
for directions in [
                     'RLRSLL',
                     'LLRR',
                     'LRSLRSRSLRRLSRLRRRSRSRLLSSSRSRLSLLLLRLSLRRLRLSLSRRLLRLSLRSSRRLLRSRSRRSLLLLLSSRRRRRRSRRSRSLSSLSSLLLSL',
                  ]:
    print(f'directions = {directions}')
    sol = Solution()
    r = sol.countCollisions(directions)
    r1 = sol.countCollisions(directions)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===========================')




