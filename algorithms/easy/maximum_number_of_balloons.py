from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cntr = Counter(text)
        ans = 0
        no_more_balloons = False
        while True:
            for ch in 'balloon':
                if cntr[ch] <= 0:
                    no_more_balloons = True
                    break
                cntr[ch] -= 1
            if no_more_balloons:
                break
            else:
                ans += 1
        return ans

# Main section
for text in [
               'nlaebolko',
               'loonbalxballpoon',
               'leetcode',
               'noollabxnoollabynoollabznoollabanoollabbnoollabcnoollab',
               'noollabnnoollabonoollabonoollablnoollablnoollabanoollabxnoollab',
               'noollabnnoollabonoollabonoollablnoollablnoollabanoollabbnoollab',
            ]:
    print(f'text = {text}')
    sol = Solution()
    r = sol.maxNumberOfBalloons(text)
    print(f'r = {r}')
    print('=================')

