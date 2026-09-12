class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 0
        
        result = []
        for i in range(k):
            largestKey = max(freqs, key=freqs.get)
            freqs.pop(largestKey)
            result.append(largestKey)
        
        return result