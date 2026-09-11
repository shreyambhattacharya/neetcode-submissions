class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for i, num in enumerate(nums):
            if target-num in seen:
                result += [seen[target-num], i]
                return result
            else:
                seen[num] = i
        
        return result