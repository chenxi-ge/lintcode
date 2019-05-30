class Solution:
    """
    @param: nums: An integer array.
    @return: nothing
    """
    def rerange(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return nums

        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < 0:
                left += 1
            while left <= right and nums[right] > 0:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        neg_count = left
        pos_count = len(nums) - right - 1
        
        # the amount of pos and neg number should at most diff by one
        if abs(neg_count - pos_count) > 1:
            return
        
        left = 1 if neg_count >= pos_count else 0
        right = len(nums) - 2 if pos_count >= neg_count else len(nums)-1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 2
            right -= 2
