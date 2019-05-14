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
