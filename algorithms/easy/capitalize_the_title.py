class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr = list()
        for word in title.split():
            if len(word) <= 2:
                arr.append(word.lower())
            else:
                arr.append(word.capitalize())
        return ' '.join(arr)

# Main section
for title in [
                'capiTalIze tHe titLe',
                'First leTTeR of EACH Word',
                'i lOve leetcode',
                'now is the time for all young men TO COME TO THE AID OF THEIR COUNTRY',
             ]:
    print(f'title = {title}')
    sol = Solution()
    r = sol.capitalizeTitle(title)
    print(f'r = {r}')
    print('=================')

