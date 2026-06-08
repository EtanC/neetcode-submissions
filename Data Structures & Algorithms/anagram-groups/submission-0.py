class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: dict[str,list] = defaultdict(list)
        # {"aet": [ate, tea]}
        for s in strs: 
            sorted_string: str = ''.join(sorted(s))
            result[sorted_string].append(s)
        return list(result.values())