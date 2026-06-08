class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, List[str]] = {}
        result: List[List[str]] = []
        
        for word in strs: 
            new_word = "".join(sorted(word))
            if new_word in groups: 
                groups[new_word].append(word)
            else: 
                groups[new_word] = [word]
            
        
        for arrays in groups.values():
            result.append(arrays)
        
        return result
