from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()  # Sort by mass in ascending order
        for asteroid in asteroids:
            # Traverse the asteroids in order, attempt to destroy and update mass or return the result
            if mass < asteroid:
                return False
            mass += asteroid
        return True  # Successfully destroy all asteroids

# Main section
for mass, asteroids in [
                          (10, [3,9,19,5,21]),
                          (5, [4,9,23,4]),
                       ]:
    print(f'mass, asteroids = {mass}, {asteroids}')
    sol = Solution()
    r = sol.asteroidsDestroyed(mass, asteroids)
    print(f'r = {r}')
    print('==============================')



