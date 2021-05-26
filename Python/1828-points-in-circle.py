class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for circle in queries:
            pointsInside = 0
            for point in points:
                distance = Solution.distanceFormula(point, circle)
                if(distance <= circle[2]):
                    pointsInside += 1
            answer.append(pointsInside)
        return answer
    
    def distanceFormula(point, circle):
        x1 = circle[0]
        y1 = circle[1]
        x2 = point[0]
        y2 = point[1]
        return(math.sqrt(((x1-x2)**2) + ((y1-y2)**2)))