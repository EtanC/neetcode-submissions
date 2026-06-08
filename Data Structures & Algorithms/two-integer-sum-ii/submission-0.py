class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force approach? 
        # given that it is non-decreasing, means that we can just loop once from left to right 
        # two pointer approach
        # establish curr
        # while curr < len(numbers) - 1
        #   if 

        num_len: int = len(numbers)
        i: int = 0
        while i < num_len:
            j: int = i + 1
            while j < num_len:
                if i == j: 
                    j += 1
                if numbers[i] + numbers[j] == target and i < j: 
                    return [i + 1, j + 1]
            i += 1 
