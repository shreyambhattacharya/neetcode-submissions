class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []

        for s in strs:
            ascend = "".join(sorted(s))
            if ascend in seen:
                seen[ascend].append(s)
            else:
                seen[ascend] = [s]
        
        for key in seen:
            result.append(seen[key])
        
        return result
