class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longestSequence = 0
        for num in numSet:
            val = num
            currentSequence = 0
            if val-1 in numSet:
                continue
            else:
                while val in numSet:
                    val += 1
                    currentSequence += 1
                longestSequence = max(longestSequence, currentSequence)
            
        return longestSequence

