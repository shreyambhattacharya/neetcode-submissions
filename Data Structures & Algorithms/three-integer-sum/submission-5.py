class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index, num in enumerate(nums):
            if index != 0 and nums[index] == nums[index-1]:
                continue
            left = index+1
            right = len(nums) - 1
            while (left < right):
                if nums[left] + nums[right] < -num:
                    left += 1
                elif nums[left] + nums[right] > -num:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        
        return result