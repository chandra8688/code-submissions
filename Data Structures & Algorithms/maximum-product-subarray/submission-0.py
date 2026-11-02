class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num<0:
                curr_max, curr_min = curr_min, curr_max
            curr_max =max(num, num* curr_max)
            curr_min = min(num, num*curr_min)
            result = max(result, curr_max)
        return result