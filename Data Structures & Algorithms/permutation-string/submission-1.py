class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force 
        # loop through s2, keep a counter of s1, reduce the counter from s1 as we loop through 

        counter1: dict[str, int] = Counter(s1)
        left: int = 0
        right: int = len(s1)
        
        while right < len(s2):
            print(Counter(s2[left:right]))
            if counter1 == Counter(s2[left:right]): 
                return True
            
            left += 1
            right += 1
        
        return False