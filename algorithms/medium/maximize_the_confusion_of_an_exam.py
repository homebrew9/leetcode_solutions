class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        N = len(answerKey)
        left, right = 0, 0
        tcount, fcount = 0, 0
        max_len = 0
        while right < N:
            if answerKey[right] == 'T':
                tcount += 1
            else:
                fcount += 1
            if min(tcount, fcount) <= k:
                max_len = max(max_len, right-left+1)
            else:
                while min(tcount, fcount) > k:
                    if answerKey[left] == 'T':
                        tcount -= 1
                    else:
                        fcount -= 1
                    left += 1
            right += 1
        return max_len

# Main section
for answerKey, k in [
                       ('TTTFTFTF', 1),
                       ('TTFF', 2),
                       ('TFFT', 1),
                       ('TTFTTFTT', 1),
                       ('TTTTTTTT', 1),
                       ('FFFFFFFF', 1),
                       ('TFFFFFFT', 1),
                       ('TFTFTFTF', 1),
                       ('TFTFTFTF', 2),
                       ('TFTFTFTF', 3),
                       ('TFTFTFTF', 4),
                    ]:
    print(f'answerKey, k = {answerKey}, {k}')
    sol = Solution()
    r = sol.maxConsecutiveAnswers(answerKey, k)
    print(f'r = {r}')
    print('===============')


