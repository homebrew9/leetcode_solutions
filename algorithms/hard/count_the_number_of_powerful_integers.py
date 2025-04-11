class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # Using combinatorial mathematics
        start_ = str(start - 1)
        finish_ = str(finish)
        return self.calculate(finish_, s, limit) - self.calculate(start_, s, limit)

    def calculate(self, x: str, s: str, limit: int) -> int:
        if len(x) < len(s):
            return 0
        if len(x) == len(s):
            return 1 if x >= s else 0

        suffix = x[len(x) - len(s) :]
        count = 0
        pre_len = len(x) - len(s)

        for i in range(pre_len):
            if limit < int(x[i]):
                count += (limit + 1) ** (pre_len - i)
                return count
            count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)

        if suffix >= s:
            count += 1

        return count

# Main section
for start, finish, limit, s in [
                                  (1, 6000, 4, '124'),
                                  (15, 215, 6, '10'),
                                  (1000, 2000, 4, '3000'),
                               ]:
    print(f'start, finish, limit, s = {start}, {finish}, {limit}, {s}')
    sol = Solution()
    r = sol.numberOfPowerfulInt(start, finish, limit, s)
    print(f'r = {r}')
    print('========================')

