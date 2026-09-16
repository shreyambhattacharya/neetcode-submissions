class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefProd = 1
        for num in nums:
            result.append(prefProd)
            prefProd *= num
        
        suffProd = 1
        for i, num in enumerate(nums[::-1]):
            result[-i-1] *= suffProd
            suffProd *= num
        
        return result


        
        