class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            results = nums[i]
            
            # FIX 1: Look at the elements AFTER 'i', up to the end of the list
            for j in range(i + 1, len(nums)):
                
                # FIX 2: Add the actual number at index j, not the index tracking number itself
                TwoSum = results + nums[j]
                
                # FIX 3: Variable names must match exactly (lowercase 's' in your check)
                if TwoSum == target:
                    # FIX 4: Return a list containing the two indices [i, j]
                    return [i, j]
                    
        # Return empty list if no pair matches the target
        return []