class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x,y = points[0][0], points[0][1]
        dist = 0
        for cord in points:   
            dist +=  max(abs(cord[0]-x),abs(cord[1]-y))
            x,y=cord[0],cord[1]
        return dist