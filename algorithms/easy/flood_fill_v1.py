from typing import List

class Solution:
    def colorCell(self, image: List[List[int]], sr: int, sc: int, newColor: int, rl: int, cl: int, oldColor: int) -> List[List[int]]:
        #print(f'    ({sr}, {sc})')
        if sr < 0 or sr >= rl:
            return image
        if sc < 0 or sc >= cl:
            return image
        if image[sr][sc] != oldColor:
            return image
        image[sr][sc] = newColor
        image = self.colorCell(image, sr, sc-1, newColor, rl, cl, oldColor)
        image = self.colorCell(image, sr, sc+1, newColor, rl, cl, oldColor)
        image = self.colorCell(image, sr-1, sc, newColor, rl, cl, oldColor)
        image = self.colorCell(image, sr+1, sc, newColor, rl, cl, oldColor)
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rlen = len(image)
        clen = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        else:
            return self.colorCell(image, sr, sc, newColor, rlen, clen, oldColor)

# Main section
for image, sr, sc, color in [
                               ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),
                               ([[0,0,0],[0,0,0]], 0, 0, 0),
                            ]:
    print(f'image = {image} ; sr, sc, color = {sr}, {sc}, {color}')
    sol = Solution()
    r = sol.floodFill(image, sr, sc, color)
    print(f'r = {r}')
    print('==========================')

