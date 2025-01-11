from typing import List

class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        N = len(sensor1)
        for i in range(N):
            if sensor1[i] != sensor2[i]:
                break

        # If one data point has been dropped from sensor2, then sensor1[i] will never
        # be found in sensor2. But sensor1[i+1:N] should match sensor2[i:N]
        # sensor1 = [1, 2, 3, 4, 5, 6, 7, 8   ]
        # sensor2 = [1, 2, 3, 4,    6, 7, 8, 9]
        j = i
        while j < N-1 and sensor1[j+1] == sensor2[j]:
            j += 1

        # Now test for the reverse situation. If one data point has been dropped from
        # sensor1, then sensor2[i] will never be found in sensor1. But sensor2[i+1:N]
        # should match sensor1[i:N]
        # sensor1 = [1, 2, 3, 4,    6, 7, 8, 10]
        # sensor2 = [1, 2, 3, 4, 5, 6, 7, 8    ]
        k = i
        while k < N-1 and sensor2[k+1] == sensor1[k]:
            k += 1
        
        # A third (ambiguous) case could also occur. If the arrays look like this:
        # sensor1 = [1, 2, 3, 2, 3, 2]
        # sensor2 = [1, 2, 3, 3, 2, 3]
        # then it could be that the 2 at end of sensor1 was a replacement for 3 at index 3:
        # sensor1 = [1, 2, 3, 3, 2, 3, (2)]
        # sensor2 = [1, 2, 3, 3, 2, 3]
        # or, it could be that the 3 at end of sensor2 was a replacement for 2 at index 3:
        # sensor1 = [1, 2, 3, 2, 3, 2]
        # sensor2 = [1, 2, 3, 2, 3, 2, (3)]
        # In this ambiguous case, j and k will both match the rest of the arrays until index N-2
        if j == N - 1 and k == N - 1:
            return -1
        elif j == N - 1:
            return 2
        elif k == N - 1:
            return 1

# Main section
for sensor1, sensor2 in [
                           ([1,2,3,2,3,2], [1,2,3,3,2,3]),
                           ([2,3,4,5], [2,1,3,4]),
                           ([2,2,2,2,2], [2,2,2,2,5]),
                           ([2,3,2,2,3,2], [2,3,2,3,2,7]),
                           ([1,2,3,2,3,2], [1,2,3,3,2,3]),
                        ]:
    print(f'sensor1, sensor2 = {sensor1}, {sensor2}')
    sol = Solution()
    r = sol.badSensor(sensor1, sensor2)
    print(f'r = {r}')
    print('================')

