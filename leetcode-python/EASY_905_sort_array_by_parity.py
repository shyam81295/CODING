# O(N) time, O(N) space complexity
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd_list = []
        even_list = []
        for elem in A:
            if elem&1 == 1:
                odd_list.append(elem)
            else:
                even_list.append(elem)
        even_list.extend(odd_list)
        return even_list
