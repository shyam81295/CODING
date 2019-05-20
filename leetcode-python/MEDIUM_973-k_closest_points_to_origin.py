# O(N + KlogN) time, O(N) space complexity
# using heapq.nsmallest() with key argument.
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans_list = []
        heapq.heapify(points)
        
        return heapq.nsmallest(K,points,key= lambda v:v[0]*v[0]+v[1]*v[1])
   
# O(N + KlogN) time, O(N) space complexity
# using tuple ordering
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        ans_list = []
        heap_list = []
        
        for i in range(len(points)):
            heap_list.append((points[i][0]*points[i][0] + points[i][1]*points[i][1],points[i]))
            
        heapq.heapify(heap_list)
        
        for i in range(K):
            tup = heapq.heappop(heap_list)
            ans_list.append(list(tup[1]))
        
        return ans_list
