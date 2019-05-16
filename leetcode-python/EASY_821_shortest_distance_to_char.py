# O(N^2) solution
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        c_indices = []
        ans_list = [float('inf')]*len(S)
        for j in range(len(S)):
            if C == S[j]:
                c_indices.append(j)
            
        for i in c_indices:
            for j in range(len(S)):
                if abs(i-j) < ans_list[j]:
                    ans_list[j] = abs(i-j)
        return ans_list
        
# O(N) solution
# calculate distance from immediate left 'C' for each element in O(N) loop
# then from immediate right 'C' for each element in O(N) loop
# for left, initialise to float('-inf') and for right, initialise to float('inf')
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans_list = [0]*len(S)
        
        prev = float('-inf')
        for i in range(len(S)):
            if S[i] == C:
                prev = i
                ans_list[i] = 0
            else:
                ans_list[i] = i-prev
                
        next = float('inf')
        for i in range(len(S)-1, -1 , -1):
            if S[i] == C:
                ans_list[i] = 0
                next = i
            else:
                ans_list[i] = min(ans_list[i],next-i)
        return ans_list
