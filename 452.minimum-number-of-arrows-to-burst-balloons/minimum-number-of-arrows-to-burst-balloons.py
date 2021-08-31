class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key=lambda x: x[1])
        pos = points[0][1]
        shot = 1
        for p in points[1:]:
            if p[0] > pos:
                shot += 1
                pos = p[1]
        return shot
