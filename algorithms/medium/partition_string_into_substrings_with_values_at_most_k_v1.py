class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        # Iterating through s from right to left
        num = int(s)
        place_value = 1
        curr = 0
        cnt = 0
        while num > 0:
            #print(f'\tnum = {num}')
            p, q = divmod(num, 10)
            if q > k:
                return -1
            num = p

            curr += q * place_value

            #print(f'\tpv, curr, k = {place_value}, {curr}, {k}')
            if curr > k:
                cnt += 1
                curr //= place_value
                place_value = 10
                #print(f'\t\tpv, updated curr = {place_value}, {curr}')
            else:
                place_value *= 10
            #print(f'\tcnt = {cnt}')
            #print('=====')
        if curr > 0:
            cnt += 1

        return cnt

# Main section
for s, k in [
               ('165462', 60),
               ('238182', 5),
               ('1234567898765432133745893', 3376),
               ('2995624428278123422153476983795874268215311982758939386251',128),
               ('5311982', 128),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.minimumPartition(s, k)
    print(f'r = {r}')
    print('================')


