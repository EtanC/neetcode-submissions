class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force approach? 
        # given that it is non-decreasing, means that we can just loop once from left to right 
        # two pointer approach
        # establish curr
        # while curr < len(numbers) - 1
        #   if 

        i:int = 0
        j:int = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target and i < j:
                return [i + 1, j + 1] 
            if numbers[i] + numbers[j] > target:
                j -= 1
            else: 
                i += 1 

