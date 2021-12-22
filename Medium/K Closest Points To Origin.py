import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for i in range(len(points)):
            distance = -1 * (math.sqrt(points[i][0]**2 + points[i][1]**2))
            points[i] = (distance, points[i][0], points[i][1])
        
        print(points)
        
        heapList = []
        for i in range(k):
            heapq.heappush(heapList, points[i])
            
        for i in range(k, len(points)):
            if points[i][0] > heapList[0][0]:
                heapq.heappop(heapList)
                heapq.heappush(heapList, points[i])
        print(heapList)
            
        retList = []
        for i in heapList:
            retList.append([i[1],i[2]])
        
        return retList
            