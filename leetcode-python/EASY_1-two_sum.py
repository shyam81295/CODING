# O(nlogn) solution
# sort list with indices, then use 2-pointers.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sorted_indices_list = sorted(range(len(nums)), key= lambda k:nums[k])
        sorted_values_list = []
        for idx in sorted_indices_list:
            sorted_values_list.append(nums[idx])
        ans_list = []
        
        i = 0
        j = len(sorted_values_list)-1
        while i<j:
            if sorted_values_list[i] + sorted_values_list[j] > target:
                j -= 1
            elif sorted_values_list[i] + sorted_values_list[j] < target:
                i+= 1
            else:
                ans_list.append(sorted_indices_list[i])
                ans_list.append(sorted_indices_list[j])
                break
                    
        return ans_list
        
