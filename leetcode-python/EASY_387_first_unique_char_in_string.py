# O(N+26) time, O(26) space complexity
# create a hashmap, and check if elem in s has count 1 from start.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = -1
        alpha_dict = {}
        order_list = []
        for i,char in enumerate(s):
            if char not in alpha_dict:
                alpha_dict[char] = 1
                order_list.append(char)
            else:
                alpha_dict[char] += 1
            
        for elem in order_list:
            if alpha_dict[elem] == 1:
                answer = s.index(elem)
                break
                
        return answer
