class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = [int(x) for x in version1.split('.')]
        arr2 = [int(x) for x in version2.split('.')]
        N, M = len(arr1), len(arr2)
        arr1 += [0] * (max(N, M) - N)
        arr2 += [0] * (max(N, M) - M)
        for a, b in zip(arr1, arr2):
            if a < b:
                return -1
            if a > b:
                return 1
        return 0

# Main section
for version1, version2 in [
                             ('1.2', '1.10'),
                             ('1.01', '1.001'),
                             ('1.0', '1.0.0.0'),
                             ('8.3.1.0.0.0.0.0.0.4', '8.3.1.0.0'),
                          ]:
    print(f'version1 = {version1}')
    print(f'version2 = {version2}')
    sol = Solution()
    r = sol.compareVersion(version1, version2)
    print(f'r = {r}')
    print('===================')



























