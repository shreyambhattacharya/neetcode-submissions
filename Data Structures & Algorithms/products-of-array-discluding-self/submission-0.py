class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = []
        prefProd = 1
        for i, num in enumerate(nums):
            prefixes.append(prefProd)
            prefProd *= num
        
        suffixes = []
        suffProd = 1
        for i, num in enumerate(nums[::-1]):
            suffixes.append(suffProd)
            suffProd *= num
        
        result = []
        for prefix, suffix in zip(prefixes, suffixes[::-1]):
            result.append(prefix * suffix)
        
        return result


        
        