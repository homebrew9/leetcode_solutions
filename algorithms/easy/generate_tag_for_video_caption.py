class Solution:
    def generateTag(self, caption: str) -> str:
        arr = caption.split()
        N = len(arr)
        res = '#'
        for i in range(N):
            if i == 0:
                res += arr[i].lower()
            else:
                res += arr[i].capitalize()
        return res[:100]

# Main section
for caption in [
                  'Leetcode daily streak achieved',
                  'can I Go There',
                  'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh',
                  'old mc donald had a farm',
                  'did kevin o leary put his money in it',
                  'the Swedish pop group ABBA had many hit songs',
               ]:
    print(f'caption = {caption}')
    sol = Solution()
    r = sol.generateTag(caption)
    print(f'r = {r}')
    print('=======================')






