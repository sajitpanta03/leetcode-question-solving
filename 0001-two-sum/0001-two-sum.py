class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            results = nums[i]
            
            for j in range(i + 1, len(nums)):
                
                TwoSum = results + nums[j]
                
                if TwoSum == target:
                    return [i, j]

        return []