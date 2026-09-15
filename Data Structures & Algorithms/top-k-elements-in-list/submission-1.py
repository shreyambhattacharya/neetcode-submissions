class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        buckets = [[] for x in range(len(nums) + 1)]
        for num in freqs:
            freq = freqs[num]
            buckets[freq].append(num)
        
        result = []
        for bucket in range(len(buckets)-1, 0, -1):
            for num in buckets[bucket]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result

        