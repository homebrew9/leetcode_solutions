class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def solve(i, arr):
            #print(f'BEGIN: i, arr = {i}, {arr}')
            if i >= N:
                return
            lvl = 0
            while i < N and input[i] == '\t':
                lvl += 1
                i += 1
            while arr and len(arr) > lvl:
                #if len(arr) == 0:
                #    break
                arr.pop()
            chunk = ''
            while i < N and input[i] != '\n':
                chunk += input[i]
                i += 1
            arr += [chunk]
            if '.' in chunk:
                self.res = max(self.res, sum([len(x) for x in arr]) + len(arr) - 1)
            #print(f'END  : i, arr = {i}, {arr}')
            #print('====')
            solve(i + 1, arr)
        N = len(input)
        self.res = 0
        arr = list()
        solve(0, arr)
        return self.res

# Main section
for input in [
                'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext',
                'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext',
                'a',
                'dir1\n\tsdir1\n\t\tfile1.ext\n\t\tanotherfile1.ext\ndir2\n\tsdir2\n\t\tareallyveryveryandextremelylongfilename1.ext\ndir3\n\tsdir3\n\tsdir4',
             ]:
    print(f'input = {input}')
    sol = Solution()
    r = sol.lengthLongestPath(input)
    print(f'r = {r}')
    print('===============')

