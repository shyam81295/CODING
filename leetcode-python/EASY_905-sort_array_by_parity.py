# O(N) time, O(N) space complexity
# if order was important, then we had to use this algorithm.
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
   
# O(N) time, O(1) space complexity
# here order was not important for even elements and odd elements
# so we can afford in-place algorithm with 2 pointers.
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A)-1
        while i < j:
            x = A[i]&1
            y = A[j]&1
            
            if x == 1 and y == 0:
                A[j],A[i] = A[i],A[j]
                i += 1
                j -= 1
            elif x == 0 and y == 1:
                i += 1
                j -= 1
            elif x == 0 and y == 0:
                i += 1
            elif x == 1 and y == 1:
                j -= 1
        return A
