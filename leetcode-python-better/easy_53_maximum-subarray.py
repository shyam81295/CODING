class Solution:
    def maxSubArray(self, nums):
        '''
        :type nums: list of list
        :rtype: int
        '''

        """
        Using Kadane's algorithm.

        2 choices =>
            1. start the run from current index.
            2. include the current index in the run.

        Base case : initialise max_overall & max_ending_here
                    with first element.
        """

        if not nums:
            return 0

        max_ending_here = nums[0]
        max_overall = nums[0]

        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_overall = max(max_ending_here, max_overall)
        return max_overall
