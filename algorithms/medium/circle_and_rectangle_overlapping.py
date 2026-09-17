class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX, closestY = None, None
        # Determine the closest x-value
        if xCenter < x1:
            closestX = x1
        elif x1 <= xCenter <= x2:
            closestX = xCenter
        else:   # xCenter > x2
            closestX = x2
        # Determine the closest y-value
        if yCenter < y1:
            closestY = y1
        elif y1 <= yCenter <= y2:
            closestY = yCenter
        else:   # yCenter > y2
            closestY = y2

        # An idiom for clamping a value into a range is as follows.
        #closestX = max(x1, min(xCenter, x2))
        #closestY = max(y1, min(yCenter, y2))
        # Goal: Find the closest value to xCenter that still lies within [x1, x2].
        # Step 1: min(xCenter, x2) => This caps xCenter from above so it never exceeds x2.
        # Step 2: This takes the result from Step 1 and caps it from below so it never goes lower than x1.

        # At this point, the closest point to the circle is (closestX, closestY)
        # If distance between the center of the circle and closest point is <= radius,
        # then the circle and rectangle overlap, otherwise they do not.
        dist_sq = (xCenter - closestX)**2 + (yCenter - closestY)**2
        return dist_sq <= radius**2

# Main section
for radius, xCenter, yCenter, x1, y1, x2, y2 in [
                                                   (1, 0, 0, 1, -1, 3, 1),
                                                   (1, 1, 1, 1, -3, 2, -1),
                                                   (1, 0, 0, -1, 0, 0, 1),
                                                   (1, 0, 0, -1, -1, 1, 1),
                                                   (1, 5, 5, 0, 0, 10, 10),
                                                   (100, 0, 0, -1, -1, 1, 1),
                                                   (5, 0, 0, 3, 4, 6, 8),
                                                   (1, 0, 0, 10, 10, 12, 12),
                                                   (1, 0, 0, 1, -5, 5, 5),
                                                   (2, -3, -3, -5, -5, -1, -1),
                                                   (2000, -10000, -10000, -10000, -10000, 10000, 10000),
                                                ]:
    print(f'radius, xCenter, yCenter, x1, y1, x2, y2 = {radius}, {xCenter}, {yCenter}, {x1}, {y1}, {x2}, {y2}')
    sol = Solution()
    r = sol.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
    print(f'r = {r}')
    print('===================================')



















