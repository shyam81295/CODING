# O(N) time, O(N) space complexity

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans_list = []
        # get next greater elements of nums2
        stack_list = []
        ans_dict = dict()
        if nums2:
            i = 0
            stack_list.append(nums2[0])
        if len(nums2) > 1:
            i = 1
            while i<len(nums2):
                while stack_list and stack_list[-1] < nums2[i]:
                    a = stack_list.pop()
                    ans_dict[a] = nums2[i]
                stack_list.append(nums2[i])
                i += 1
            while stack_list:
                a = stack_list.pop()
                ans_dict[a] = -1

        # for each elem in nums1, get value from map, append into answer_list
        for elem in nums1:
            ans_list.append(ans_dict[elem])
        return ans_list
        
        
        
        
